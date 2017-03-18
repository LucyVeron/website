#!/usr/bin/python
#server.py
from wsgiref.handlers import CGIHandler
from server import app

CGIHandler().run(app)
