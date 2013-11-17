from app import app
import flask, flask.views

from database import connection, models

@app.route('/')
def home():
	entries = connection.session.query(models.Entry).all()
	return flask.render_template('index.html', entries = entries);