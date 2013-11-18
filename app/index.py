from app import app
import flask, flask.views

from database import connection, models

@app.route('/')
def home():
	entries = connection.session.query(models.Entry).all()
	return flask.render_template('index.html', entries = entries);

@app.route('/jar/<int:id>')
def list_by_jar(jar_id):
	return 'foo'

@app.route('/version/<string:name>')
def list_by_version(version_name):
	return 'foo'
