from sqlalchemy import Column, Integer, DateTime, String, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
import connection
from .. import config

class Entry(connection.Base):
	__tablename__ = 'entries'

	id = Column(Integer, primary_key = True)
	jar_id = Column(Integer, ForeignKey('jars.id'))
	version = Column(String(10))
	votes_up = Column(Integer, default = 0)
	votes_down = Column(Integer, default = 0)
	created_at = Column(DateTime, default = datetime.now)

	def __repr__(self):
		return "<Entry(jar_id='%s', votes_up='%s', votes_down='%s', created_at='%s')>" % (self.jar_id, self.votes_up, self.votes_down, self.created_at)

class Jar(connection.Base):
	__tablename__ = 'jars'

	id = Column(Integer, primary_key = True)
	name = Column(String(20))
	entries = relationship("Entry", backref = "entries")

	def __repr__(self):
		return "<Jar(name='%s')>" % (self.name)


def migrate():
	for tbl in reversed(connection.Base.metadata.sorted_tables):
		tbl.drop(connection.engine)

	connection.Base.metadata.create_all(connection.engine)

	for jar in config.jars:
		add = Jar(name = jar)
		connection.session.add(add)

	connection.session.commit()