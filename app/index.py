from app import app
import flask, flask.views

class View(flask.views.MethodView):
	def get(self):
		return flask.render_template('index.html');

app.add_url_rule('/', view_func = View.as_view('main'))