from app import app
import flask, flask.views

class GeneratorView(flask.views.MethodView):
	def get(self):
		return flask.render_template('generate.html');

app.add_url_rule('/create', view_func = GeneratorView.as_view('create'))