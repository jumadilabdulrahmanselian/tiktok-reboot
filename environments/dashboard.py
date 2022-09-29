from flask import Blueprint, render_template, request, jsonify, session, redirect
dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/dashboard')
def dashboardPage():
    if not session.get("AS_USER"):
        return redirect(request.host_url+"auth/login")
    javascript = []
    java = []
    css = []
    return render_template("dashboard/dashboard.html", javascript=javascript, java=java, css=css)
