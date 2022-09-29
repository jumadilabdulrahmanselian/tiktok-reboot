from flask import Flask, request
from flask_session import Session
import sys

def init_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'lasdailshdlasdnalskdn'
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"
    if sys.platform == 'linux' or sys.platform == 'linux2':
        app.config["SESSION_FILE_DIR"] = "/home/alimstudio/Applications/python/tiktok-python/flask_session/"
    Session(app)

    from .auth import auth
    from .dashboard import dashboard
    from .parent import parent
    from .username import username

    app.register_blueprint(auth, url_prefix='/auth/')
    app.register_blueprint(dashboard, url_prefix='/admin/')
    app.register_blueprint(parent, url_prefix='/admin/')
    app.register_blueprint(username, url_prefix='/admin/')
    return app

def base_uri():
    return request.host_url