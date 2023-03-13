from flask import Blueprint, render_template, request, jsonify, session, redirect, send_file
from .services.api import get, getPost
from .services.database.dbtiktok import getUsernameByUser, isUsernameExist, saveUsername, getFromHistory, saveVideo, getVideosByUsername
import requests
import random,os
import string  

tiktok = Blueprint('tiktok', __name__)

@tiktok.route('/tiktok/videos')
def videosPage():
    if not session.get("AS_USER"):
        return redirect(request.host_url+"auth/login")
    css = [
        'plugins/datatables.net-bs5/css/dataTables.bootstrap5.min.css',
        'plugins/datatables.net-buttons-bs5/css/buttons.bootstrap5.min.css',
        'plugins/datatables.net-responsive-bs5/css/responsive.bootstrap5.min.css',
        'plugins/bootstrap-table/dist/bootstrap-table.min.css'
    ]
    javascript = [
        "plugins/@highlightjs/cdn-assets/highlight.min.js",
        "js/demo/highlightjs.demo.js",
        "plugins/datatables.net/js/jquery.dataTables.min.js",
        "plugins/datatables.net-bs5/js/dataTables.bootstrap5.min.js",
        "plugins/datatables.net-buttons/js/dataTables.buttons.min.js",
        "plugins/datatables.net-buttons/js/buttons.colVis.min.js",
        "plugins/datatables.net-buttons/js/buttons.flash.min.js",
        "plugins/datatables.net-buttons/js/buttons.html5.min.js",
        "plugins/datatables.net-buttons/js/buttons.print.min.js",
        "plugins/datatables.net-buttons-bs5/js/buttons.bootstrap5.min.js",
        "plugins/datatables.net-responsive/js/dataTables.responsive.min.js",
        "plugins/datatables.net-responsive-bs5/js/responsive.bootstrap5.min.js",
        "plugins/bootstrap-table/dist/bootstrap-table.min.js"
    ]
    java = [
        "module/tiktok/tiktok.js"
    ]
    # print(java)
    return render_template("tiktok/videos.html", javascript=javascript, java=java, css=css)

@tiktok.route('/username/load', methods=["POST"])
def getUsername():
    if not session.get("AS_USER"):
        return jsonify({"status": False, "header":"Hehehe!", "message": "Failed to fetch data"})
    else:
        try:
            data = request.form
            scrty = data["scrty"]
            
            if scrty == 'true':
                headers = {
                    'x-api-key':'78a892ce570eca1f8c17b56f3a35ccd97977ce02',
                    'x-app-key':'dcdf567f-610e-59a6-8297-80c5a99eafdc'
                }
                if session['AS_USER'][5] == 'ADMIN':
                    response = get("http://localhost:3000/tik/username", headers=headers)
                else:
                    response = getPost("http://localhost:3000/tik/username", headers=headers, data={'uid':session['AS_USER'][0]})

                if response['status'] is True:
                    return jsonify({"status": True, "header": "Berhasil!", "data": response['data']})
                # response = getUsernameByUser(session['AS_USER'][0], session['AS_USER'][5])
                # if len(response) > 0:
                #     return jsonify({"status": True, "header": "Berhasil!", "data": response})
                else:
                    return jsonify({"status": False, "header": "Yaah!", "message": "Failed to fetch data"})
            else:
                return jsonify({"status": False, "header": "Yaah!", "message": "Failed to Authenticate"})
        except Exception as e:
            return jsonify({"status": False, "header": "Remember!", "message": "Api Server Down"})

@tiktok.route('/videos/load', methods=["POST"])
def getVideos():
    if not session.get("AS_USER"):
        return jsonify({"status": False, "header":"Hehehe!", "message": "Failed to fetch data"})
    else:
        try:
            data = request.form
            scrty = data["scrty"]
            username = data["username"]
            
            if scrty == 'true':
                response = getVideosByUsername(username)
                print(username)
                if len(response) > 0:
                    return jsonify({"status": True, "header": "Berhasil!", "data": response})
                else:
                    return jsonify({"status": False, "header": "Yaah!", "message": "Failed to fetch data"})
            else:
                return jsonify({"status": False, "header": "Yaah!", "message": "Failed to Authenticate"})
        except Exception as e:
            return jsonify({"status": False, "header": "Remember!", "message": "Api Server Down"})

def random_string(letter_count, digit_count):  
    str1 = ''.join((random.choice(string.ascii_letters) for x in range(letter_count)))  
    str1 += ''.join((random.choice(string.digits) for x in range(digit_count)))  
  
    sam_list = list(str1) # it converts the string to list.  
    random.shuffle(sam_list) # It uses a random.shuffle() function to shuffle the string.  
    final_string = ''.join(sam_list)  
    return final_string  

@tiktok.route('/videos/fetch/online', methods=["POST"])
def getAllvideosOnline(tryed=1):
    # if not session.get("AS_USER"):
    #     return jsonify({"status": False, "header":"Failed Login!", "message": "Please Login First"})
    # else:
        try:
            data = request.form
            scrty = data["scrty"]
            username = data['username']
            if scrty == 'true' or scrty == True:
                if username != "":
                    isExist = isUsernameExist(username)
                    if isExist is False:
                        crawlUsernameData = get("http://localhost:2001/api/user/info/{}".format(username))
                        if crawlUsernameData['status'] is True:
                            if crawlUsernameData['avatar'] != "":
                                imgUrl = crawlUsernameData['avatar']
                                img = requests.request(method='GET', url=imgUrl)
                                avatar = img.content
                                randomString = random_string(15, 50)
                                path = "environments/static/img/tiktok/"
                                fileName = '{}-{}-{}.png'.format('TT',username, randomString)
                                # fileName = '{}-{}.jpg'.format('TT', randomString)
                                filepath = os.path.join(path, fileName)
                                with open (filepath, 'wb') as f:
                                    f.write(avatar)
                                # "data:image/png;base64,"+
                                avatar = fileName
                            else:
                                avatar = ""

                            saveUser = saveUsername(username=username, status='CRAWL', foto=avatar, nickname=crawlUsernameData['nickname'], signature=crawlUsernameData['signature'])
                            # if saveUser is True:
                            usedUsername = username
                        else:
                            return jsonify({"status": False, "header": "Yaah!", "message": "Username not registered in tiktok"})
                    else:
                        historyCheck = getFromHistory(username)
                        if historyCheck is not None and len(historyCheck) > 0:
                            usedUsername = historyCheck[2]
                        else:
                            usedUsername = username
                    res = get("http://localhost:2001/api/user/video/{}".format(username))
                    # print(res['status'])
                    if res["status"] is True:
                        numbro = 1
                        for video in res["videos"]:
                            print("{}. {}".format(numbro, video))
                            videoID = video.replace("https://www.tiktok.com/@{}/video/".format(username), "")
                            saveVideo(videoID, username, video)
                            numbro+=1
                        numbro = 1
                        return jsonify({"status": True, "header": "Horeee!", "message": "Sucessfully Fetching Data Online", "total": len(res["videos"])})
                    else: 
                        if tryed <= 3: 
                            tryed+=1
                            return getAllvideosOnline(tryed)
                        else:
                            return jsonify({"status": False, "header": "Yaah!", "message": "Failed to fetch data"})
                else:
                    return jsonify({"status": False, "header": "Wait!", "message": "Username cant be empty"})
            else:
                return jsonify({"status": False, "header": "Yaah!", "message": "Failed to Get Data"})
        except Exception as e:
            print(e)
            return jsonify({"status": False, "header": "Remember!", "message": "Api Server Down"})
        
@tiktok.route('/tiktok/username/save', methods=["POST"])
def saveUsernameImport():
    try:
        data = request.form
        scrty = data["scrty"]
        username = data['username']
        if scrty == 'true' or scrty == True:
            if username != "":
                isExist = isUsernameExist(username)
                if isExist is False:
                    crawlUsernameData = get("http://localhost:2001/api/user/info/{}".format(username))
                    if crawlUsernameData['status'] is True:
                        if crawlUsernameData['avatar'] != "":
                            imgUrl = crawlUsernameData['avatar']
                            img = requests.request(method='GET', url=imgUrl)
                            avatar = img.content
                            randomString = random_string(15, 50)
                            path = "environments/static/img/tiktok/"
                            fileName = '{}-{}-{}.png'.format('TT',username, randomString)
                            # fileName = '{}-{}.jpg'.format('TT', randomString)
                            filepath = os.path.join(path, fileName)
                            with open (filepath, 'wb') as f:
                                f.write(avatar)
                            # "data:image/png;base64,"+
                            avatar = fileName
                        else:
                            avatar = ""

                        saveUser = saveUsername(username=username, status='CRAWL', foto=avatar, nickname=crawlUsernameData['nickname'], signature=crawlUsernameData['signature'])
                        if saveUser is True:
                            return jsonify({"status": True, "header": "Horeee!", "message": "Sucessfully save username"})
                        else:
                            return jsonify({"status": False, "header": "Yaah!", "message": "Failed to save username"})
                    else:
                        return jsonify({"status": False, "header": "Yaah!", "message": "Username not registered in tiktok"})
                else:
                    return jsonify({"status": False, "header": "Wait!", "message": "Username already exist on system"})
            else:
                return jsonify({"status": False, "header": "Heemmm!", "message": "Username can't be empty"})
    except Exception as e:
        print(e)
        return jsonify({"status": False, "header": "Remember!", "message": "Api Server Down"})
    
@tiktok.route("/file", methods=["GET"])
def loadFile():
    file = request.args.get('path')
    return send_file(
         file,
         mimetype="video/mp4",
         as_attachment=True, 
         )