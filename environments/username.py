from flask import Blueprint, render_template, request, jsonify, session, redirect
# from .services.api import get, post, put, delete
username = Blueprint('username', __name__)

@username.route('/username')
def usernamePage():
    if not session.get("AS_USER"):
        return redirect(request.host_url+"auth/login")
    css = [
        'libs/datatables/css/dataTables.bootstrap5.min.css',
        'libs/datatables/css/responsive.bootstrap.min.css',
        'libs/datatables/css/buttons.dataTables.min.css',
        'libs/select2/css/select2.min.css'
    ]
    javascript = [
        'libs/datatables/js/jquery-3.6.0.min.js',
        'libs/datatables/js/jquery.dataTables.min.js',
        'libs/datatables/js/dataTables.bootstrap5.min.js',
        'libs/datatables/js/dataTables.responsive.min.js',
        'libs/datatables/js/dataTables.buttons.min.js',
        'libs/select2/js/select2.min.js'
    ]
    java = [
        'username/username.js'
    ]
    return render_template("username/username.html", javascript=javascript, java=java, css=css)

# @username.route('/username/load', methods=["POST"])
# def getAllUsername():
#     if not session.get("AS_USER"):
#         return jsonify({"status": False, "header":"Hehehe!", "message": "Failed to fetch data"})
#     else:
#         try:
#             data = request.form
#             parent = data["parent"]
#             scrty = data["scrty"]
            
#             if scrty == 'true':
#                 if parent == 'all':
#                     response = get('tiktok/username')
#                 else:
#                     response = get('tiktok/username/{}/from'.format(parent))
                    
#                 res = response.json()
#                 if res["status"] is True:
#                     return jsonify({"status": True, "header": "Berhasil!", "data": res["data"]})
#                 else:
#                     return jsonify({"status": False, "header": "Yaah!", "message": "Failed to fetch data"})
#             else:
#                 return jsonify({"status": False, "header": "Yaah!", "message": "Failed to Authenticate"})
#         except Exception as e:
#             return jsonify({"status": False, "header": "Remember!", "message": "Api Server Down"})



# @username.route('/username/save', methods=["POST"])
# def saveUsername():
#     if not session.get("AS_USER"):
#         return jsonify({"status": False, "header":"Hehehe!", "message": "Failed to fetch data"})
#     else:
#         try:
#             data = request.form
#             uname = data["uname"]
#             scrty = data["scrty"]

#             if scrty == 'true':
#                 dataBuild = {
#                     "username" : uname,
#                 }

#                 response = post('tiktok/username', dataBuild)
#                 res = response.json()
#                 if res["status"] is True:
#                     return jsonify({"status": True, "header": "Berhasil!", "message": "Berhasil Menyimpan Data"})
#                 else:
#                     return jsonify({"status": False, "header": "Yaah!", "message": "Failed to fetch data"})
#             else:
#                 return jsonify({"status": False, "header": "Yaah!", "message": "You dont have access this API"})
#         except Exception as e:
#             return jsonify({"status": False, "header": "Remember!", "message": e})

# @username.route('/username/update', methods=["POST"])
# def updateUsername():
#     if not session.get("AS_USER"):
#         return jsonify({"status": False, "header":"Hehehe!", "message": "Failed to fetch data"})
#     else:
#         try:
#             data = request.form
#             id = data["id"]
#             username = data["username"]
#             is_banned = data["is_banned"]
#             is_crawl = data["is_crawl"]
#             is_private = data["is_private"]
#             scrty = data["scrty"]
            
#             if scrty == 'true':
#                 dataBuild = {
#                     "id" : id,
#                     "username" : username,
#                     "is_crawl" : is_crawl,
#                     "is_banned": is_banned,
#                     "is_private": is_private
#                 }

#                 response = put('tiktok/username', dataBuild)
#                 res = response.json()
#                 if res["status"] is True:
#                     return jsonify({"status": True, "header": "Berhasil!", "message": "Berhasil Mengupdate Data"})
#                 else:
#                     return jsonify({"status": False, "header": "Yaah!", "message": "Failed to fetch data"})
#             else:
#                 return jsonify({"status": False, "header": "Yaah!", "message": "You dont have access this API"})
#         except Exception as e:
#             return jsonify({"status": False, "header": "Remember!", "message": "Api Server Down"})


# @username.route('/username/delete', methods=["POST"])
# def deleteUsername():
#     if not session.get("AS_USER"):
#         return jsonify({"status": False, "header":"Hehehe!", "message": "Failed to fetch data"})
#     else:
#         try:
#             data = request.form
#             id = data["id_delete"]
#             scrty = data["scrty"]
            
#             if scrty == 'true':
#                 dataBuild = {
#                     "id" : id,
#                 }

#                 response = delete('tiktok/username', dataBuild)
#                 res = response.json()
#                 if res["status"] is True:
#                     return jsonify({"status": True, "header": "Berhasil!", "message": "Berhasil Menghapus Data"})
#                 else:
#                     return jsonify({"status": False, "header": "Yaah!", "message": "Failed to fetch data"})
#             else:
#                 return jsonify({"status": False, "header": "Yaah!", "message": "You dont have access this API"})
#         except Exception as e:
#             return jsonify({"status": False, "header": "Remember!", "message": "Api Server Down"})

