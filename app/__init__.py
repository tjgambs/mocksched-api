#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config.from_object("config")

db = SQLAlchemy(app)

from app.controllers import default
from app.controllers.v1.search import search

app.register_blueprint(default.mod)
app.register_blueprint(search.mod)
