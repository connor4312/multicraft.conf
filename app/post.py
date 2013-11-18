from app import app
import os
import flask
from flask import Response, request

from database import connection, models


def user_has_voted(entry_id):
	num = connection.session.query(models.Vote).filter(models.Vote.entry_id == entry_id, models.Vote.ip == request.remote_addr).count()
	if num == 0:
		return False
	else:
		return True

@app.route('/conf/<int:entry_id>')
def show_conf_file(entry_id):
	entry = connection.session.query(models.Entry).filter(models.Entry.id == entry_id).first()

	if not entry:
		return '404'

	data = ''
	with open(os.path.dirname(os.path.realpath(__file__)) + '/../storage/post' + str(entry.id) + '.txt', 'r') as inputf:
		data = inputf.read()

	return flask.render_template('post.html', entry = entry, data = data, voted = user_has_voted(entry_id));

@app.route('/conf/<int:entry_id>/raw')
def show_conf_file_raw(entry_id):

	try:
		with open('storage/post' + str(entry_id) + '.txt', 'r') as inputf:
			return Response(inputf.read(), mimetype="text/plain")
	except IOError:
		print '404'

@app.route('/conf/<int:entry_id>/vote/<string:direction>', methods = ['POST'])
def vote_for_conf(entry_id, direction):
	if (user_has_voted(entry_id = entry_id)):
		return 'You already voted!'

	entry = connection.session.query(models.Entry).filter(models.Entry.id == entry_id).first()

	if not entry:
		return '404'

	if direction == 'up':
		entry.votes_up += 1
	elif direction == 'down':
		entry.votes_down += 1
	else:
		return 'Direction must be up or down, what\'re doing over there?'

	vote = models.Vote(entry_id = entry_id, ip = request.remote_addr)

	connection.session.add(vote)
	connection.session.commit()

	return 'OK'