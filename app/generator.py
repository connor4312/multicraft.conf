from app import app

import flask
from flask import render_template, request

@app.route('/create', methods = ['GET', 'POST'])
def show_view():

	if request.method == 'GET':
		return flask.render_template('generate.html');

	if request.method == 'POST':

		parts = []
		output = ''

		for item in request.form:
			section, attribute = item[0].split('_', 1)
			parts[section][attribute] = item[1]

		for section, attributes in parts:
			output += '[' + section + ']'
			for attribute, value in attributes:
				output += '\n' + attribute + '=' + value

		return output