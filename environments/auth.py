import hashlib
from .services.api import post
from flask import Blueprint, render_template, request, jsonify, session, redirect
auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    if session.get("AS_USER"):
        return redirect(request.host_url+"admin/dashboard")
    return render_template("auth/auth.html")

def encrypt_string(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature

@auth.route('/authorize', methods=["POST"])
def authorize():
    data = request.form
    username = data["username"]
    password = data["password"]
    scrty = data["scrty"]
    
    if scrty == 'true':
        try:
            dataBuild = {
                "username" : username,
                "password" : encrypt_string(password)
            }
            response = post('auth/authorize', dataBuild)
            res = response.json()
            if res["status"] is True:
                session["AS_USER"] = res["data"]
                return jsonify({"status": True, "header": "Berhasil!", "message": "Successfully Login"})
            else:
                return jsonify({"status": False, "header": "Yaah!", "message": "Failed to Authenticate"})
        except Exception as e:
            return jsonify({"status": False, "header": "Remember!", "message": "Api Server Down"})
    else:
        return jsonify({"status": False, "header": "Yaah!", "message": "Failed to Authenticate"})

@auth.route('/logout')
def logout():
    session['AS_USER'] = None
    return redirect(request.host_url+'auth/login')