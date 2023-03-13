from flask import Blueprint, render_template, request, jsonify, session, redirect
dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/dashboard')
def dashboardPage():
    if not session.get("AS_USER"):
        return redirect(request.host_url+"auth/login")
    css = [
        'plugins/jvectormap-next/jquery-jvectormap.css'
    ]
    javascript = [
        'plugins/jquery/dist/jquery.min.js',
        'plugins/jvectormap-next/jquery-jvectormap.min.js',
        'plugins/jvectormap-content/world-mill.js',
        'plugins/apexcharts/dist/apexcharts.min.js',
        'js/demo/dashboard.demo.js'
    ]
    java = []
    return render_template("dashboard/dashboard.html", javascript=javascript, java=java, css=css)
