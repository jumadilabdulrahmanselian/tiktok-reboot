from environments import init_app, base_uri

app = init_app()

@app.context_processor
def context_processor():
    return dict(baseUri=base_uri())

if __name__ == '__main__':
    app.run(debug=True, port=2001, host="0.0.0.0")
