from flask import Blueprint, render_template, request, jsonify, session, redirect
from .services.api import get
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

@username.route('/username/load', methods=["POST"])
def getAllUsername():
    if not session.get("AS_USER"):
        return jsonify({"status": False, "header":"Hehehe!", "message": "Failed to fetch data"})
    else:
        try:
            data = request.form
            parent = data["parent"]
            scrty = data["scrty"]
            
            if scrty == 'true':
                if parent == 'all':
                    response = get('tiktok/username')
                else:
                    response = get('tiktok/username/{}/from'.format(parent))
                    
                res = response.json()
                if res["status"] is True:
                    return jsonify({"status": True, "header": "Berhasil!", "data": res["data"]})
                else:
                    return jsonify({"status": False, "header": "Yaah!", "message": "Failed to fetch data"})
            else:
                return jsonify({"status": False, "header": "Yaah!", "message": "Failed to Authenticate"})
        except Exception as e:
            return jsonify({"status": False, "header": "Remember!", "message": "Api Server Down"})