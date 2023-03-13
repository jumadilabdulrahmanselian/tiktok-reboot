import hashlib, json
from .services.db import DB as database
from .services.database import dbauth as authdb
from flask import Blueprint, render_template, request, jsonify, session, redirect
auth = Blueprint('auth', __name__)
db = database()

@auth.route('/')
def redirectTo():
    return redirect(request.host_url+"auth/login")

@auth.route('/login')
def login():
    db.createTables()
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
    email = data["email"]
    password = data["password"]
    scrty = data["scrty"]
    
    if scrty == 'true':
        try:
            response = authdb.authorize(email, encrypt_string(password))
            print(response)
            if len(response) > 0:
                session["AS_USER"] = response
                return json.dumps({"status": True, "header": "Berhasil!", "message": "Successfully Login"})
            else:
                return json.dumps({"status": False, "header": "Yaah!", "message": "Failed to Authenticate"})
        except Exception as e:
            return json.dumps({"status": False, "header": "Remember!", "message": "Api Server Down"})
    else:
        return json.dumps({"status": False, "header": "Yaah!", "message": "Failed to Authenticate"})

@auth.route('/logout')
def logout():
    session['AS_USER'] = None
    return redirect(request.host_url+'auth/login')