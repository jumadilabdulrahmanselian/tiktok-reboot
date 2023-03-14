from flask import Blueprint, redirect, request
from .services.db import DB as dbase
data = Blueprint('data', __name__)

@data.route('/create')
def createTable():
    return redirect(request.host_url+"auth/login")

@data.route('/restore')
def restoreTable():
    return redirect(request.host_url+"auth/login")

@data.route('/reload')
def reloadTable():
    return redirect(request.host_url+"auth/login")

@data.route('/backup')
def backupTable():
    return redirect(request.host_url+"auth/login")
