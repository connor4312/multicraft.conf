#!flask/bin/python
from app.database import models
print 'Starting migrations...'
models.migrate()
print 'Ok!'