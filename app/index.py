from app import app
import flask, flask.views

from database import connection, models

@app.route('/')
def home():
	entries = connection.session.query(models.Entry).all()
	return flask.render_template('index.html', entries = entries, title = 'All Configs');

@app.route('/jar/<int:id>')
def list_by_jar(id):
	entries = connection.session.query(models.Entry).filter(models.Entry.jar_id == id).all()
	jar = connection.session.query(models.Jar).filter(models.Jar.id == id).first()
	return flask.render_template('index.html', entries = entries, title = 'Configs for ' + jar.name);

@app.route('/version/<string:name>')
def list_by_version(name):
	entries = connection.session.query(models.Entry).filter(models.Entry.version == name).all()
	return flask.render_template('index.html', entries = entries, title = 'Configs for version ' + name);
