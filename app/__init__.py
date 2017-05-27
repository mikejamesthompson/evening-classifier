#!/usr/bin/python
# -*- coding: utf-8 -*-

from os import environ

from flask import Flask, url_for, redirect

from flask_sqlalchemy import SQLAlchemy

# Initiate app
app = Flask(__name__)
app.config.from_object('app.config.development)

# Initiate DB
db = SQLAlchemy(app)

from app import views, models
