from flask import Flask, request
from flask_session import Session
import sys
from flask_compress import Compress

def init_app():
    app = Flask(__name__)
    Compress(app)
  
    app.config['SECRET_KEY'] = 'lasdailshdlasdnalskdn'
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"
    if sys.platform == 'linux' or sys.platform == 'linux2':
        app.config["SESSION_FILE_DIR"] = "/home/alimstudio/Applications/python/tiktok-python/flask_session/"
    Session(app)

    from .default import default
    from .auth import auth
    from .dashboard import dashboard
    from .parent import parent
    from .username import username
    from .api import api
    from .tiktok import tiktok
    from .database import data

    app.register_blueprint(default, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/auth/')
    app.register_blueprint(dashboard, url_prefix='/admin/')
    app.register_blueprint(tiktok, url_prefix='/admin/')
    app.register_blueprint(parent, url_prefix='/admin/')
    app.register_blueprint(username, url_prefix='/admin/')
    app.register_blueprint(api, url_prefix='/api/')
    app.register_blueprint(data, url_prefix='/database/')
    return app

def base_uri():
    return request.host_url