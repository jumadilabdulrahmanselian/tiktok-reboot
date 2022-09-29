from flask import Flask, request
from flask_session import Session
def init_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'lasdailshdlasdnalskdn'
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"
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