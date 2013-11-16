from app import app
import flask, flask.views, request

class GeneratorView(flask.views.MethodView):
	def get(self):
		return flask.render_template('generate.html');

	def post(self):

		parts = []
		output = ''

		for name, value in request.form:
			section, attribute = name.split('_', 1)
			parts[section][attribute] = value

		for section, attributes in parts:
			output += '[' + section + ']'
			for attribute, value in attributes:
				output += '\n' + attribute + '=' + value

		return output


app.add_url_rule('/create', view_func = GeneratorView.as_view('create'), methods = ['GET', 'POST'])