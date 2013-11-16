from app import app
import flask, flask.views

@app.route('/')
def home():
	return flask.render_template('index.html');