from app import app

import flask
from flask import render_template, request

@app.route('/create', methods = ['GET', 'POST'])
def show_view():

	if request.method == 'GET':
		return flask.render_template('generate.html');

	if request.method == 'POST':

		parts = {}
		output = ''

		for name, value in request.form.iteritems():
			section, attribute = name.split('_', 1)
			if section not in parts:
				parts[section] = {}

			parts[section][attribute] = value

		for section, attributes in parts.iteritems():
			output += '[' + section + ']\n'

			for attribute, value in attributes.iteritems():
				output += attribute + '=' + value + '\n'

		return output