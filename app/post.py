from app import app

import flask

from database import connection, models

@app.route('/conf/<int:entry_id>')
def show_conf_file(entry_id):
	entry = connection.session.query(models.Entry).filter(models.Entry.id == entry_id).first()

	if not entry:
		return '404'

	data = ''
	with open('storage/post' + str(entry.id) + '.txt', 'r') as inputf:
		data = inputf.read()

	return flask.render_template('post.html', entry = entry, data = data);