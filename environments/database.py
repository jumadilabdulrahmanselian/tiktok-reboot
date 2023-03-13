from flask import Blueprint, redirect, request
from .services.db import DB as dbase
database = Blueprint('database', __name__)

@database.route('/')
def redirectKe():
    return redirect(request.host_url+"auth/login")
