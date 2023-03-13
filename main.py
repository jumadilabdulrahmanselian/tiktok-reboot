from environments import init_app, base_uri
from flask import render_template, request, send_from_directory, make_response

app = init_app()

@app.context_processor
def context_processor():
    return dict(baseUri=base_uri())

@app.errorhandler(404)
def not_found(e):
    return render_template("error/404.html")

@app.route('/robots.txt')
@app.route('/sitemap.xml')
@app.route('/manifest.json')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

@app.route('/sw.js')
def sw():
    response=make_response(send_from_directory(directory='static', path='sw.js'))
    #change the content header file. Can also omit; flask will handle correctly.
    response.headers['Content-Type'] = 'application/javascript'
    return response

if __name__ == '__main__':
    app.run(debug=True, port=2001, host="0.0.0.0")
