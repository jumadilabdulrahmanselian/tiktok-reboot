from flask import Blueprint, redirect, request
default = Blueprint('default', __name__)

@default.route('/')
def redirectKe():
    return redirect(request.host_url+"/auth/login")
