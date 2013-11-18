from sqlalchemy import Column, Integer, DateTime, String, ForeignKey
from sqlalchemy.orm import relationship

from datetime import datetime

from .. import config

import connection
import re

class Entry(connection.Base):
	__tablename__ = 'entries'

	id = Column(Integer, primary_key = True)
	jar_id = Column(Integer, ForeignKey('jars.id'))
	version = Column(String(10))
	description = Column(String(200))
	votes_up = Column(Integer, default = 0)
	votes_down = Column(Integer, default = 0)
	created_at = Column(DateTime, default = datetime.now)

	jar = relationship("Jar", backref = "entry")
	votes = relationship("Vote", backref = "entry")

	def __repr__(self):
		return "<Entry(jar_id='%s', votes_up='%s', votes_down='%s', created_at='%s')>" % (self.jar_id, self.votes_up, self.votes_down, self.created_at)

	def validate(self, form):
		if not connection.session.query(Jar).filter(Jar.id == self.jar_id).count():
			return 'Invalid jar file selected.'
		if not re.match(r'^[0-9]\.[0-9](\.[0-9])?$', self.version):
			return 'You must enter a valid Minecraft version number!'
		if len(form.get('opt_config_name')) < 2:
			return 'You have to enter a good jar name!'
		if not re.match(r'^(http|https|ftp):\/\/[A-z\-\_\.\/0-9\:]+\.(zip|jar)$', form.get('opt_config_source')):
			return 'You have not entered a valid URL. Be sure you are linking to either a .zip or a .jar file. Otherwise, Multicraft will be confused!'


class Jar(connection.Base):
	__tablename__ = 'jars'

	id = Column(Integer, primary_key = True)
	name = Column(String(20))
	entries = relationship("Entry", backref = "jars")

	def __repr__(self):
		return "<Jar(name='%s')>" % (self.name)

class Vote(connection.Base):
	__tablename__ = 'votes'

	id = Column(Integer, primary_key = True)
	ip = Column(String(45))
	entry_id = Column(Integer, ForeignKey('entries.id'))

	def __repr__(self):
		return "<Jar(entry_id='%s', ip='%s')>" % (self.entry_id, self.ip)

def migrate():
	connection.Base.metadata.drop_all(connection.engine)

	connection.Base.metadata.create_all(connection.engine)

	for jar in config.jars:
		add = Jar(name = jar)
		connection.session.add(add)

	connection.session.commit()