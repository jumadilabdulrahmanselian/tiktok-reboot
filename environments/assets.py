from flask import Blueprint, url_for
assets = Blueprint('assets', __name__)

@assets.route('/assets/<any>')
def getAssets(any):
    {{ url_for('static', filename=any) }}
    return {}
