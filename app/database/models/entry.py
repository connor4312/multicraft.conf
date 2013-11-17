from sqlalchemy.ext.declarative import Column, Integer, DateTime
from .. import connection

class Entry(connection.Base):
	__tablename__ = 'entries'

	id = Column(Integer, primary_key = True)
	jar_id = Column(Integer)
	votes_up = Column(Integer)
	votes_down = Column(Integer)
	created_at = Column(DateTime)

	def __repr__(self):
		return "<Entry(jar_id='%s', votes_up='%s', votes_down='%s', created_at='%s')>" % (self.jar_id, self.votes_up, self.votes_down, self.created_at)