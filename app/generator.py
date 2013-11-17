from app import app

import flask
from flask import request

from database import connection, models

def generateFromIterator(iterator):

	parts = {}
	output = ''

	for name, value in iterator.iteritems():
		section, attribute = name.split('_', 1)
		if section not in parts:
			parts[section] = {}

		parts[section][attribute] = value

	for section, attributes in parts.iteritems():
		output += '\n[' + section + ']\n'

		for attribute, value in attributes.iteritems():

			if not value:
				output += '#'

			output += attribute + ' = ' + value + '\n'

	return output.strip('\n\r ')


@app.route('/create', methods = ['GET', 'POST'])
def show_view():

	if request.method == 'GET':
		jars = connection.session.query(models.Jar).all()
		return flask.render_template('generate.html', jars = jars);

	if request.method == 'POST':
		model = models.Entry(jar_id = 0, version = '1')
		connection.session

@app.route('/create/raw', methods = ['POST'])
def preview_generate_file():
	return generateFromIterator(request.form)
