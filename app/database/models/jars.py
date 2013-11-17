from sqlalchemy.ext.declarative import Column, String, Integer
from .. import connection

class Jars(connection.Base):
	__tablename__ = 'jars'

	id = Column(Integer, primary_key = True)
	name = Column(String)

	def __repr__(self):
		return "<Jar(name='%s')>" % (self.name)