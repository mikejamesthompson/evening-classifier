#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

from app import app

app.run(host=app.config['HOST'],
        port=app.config['PORT'],
        debug=app.config['DEBUG'],
        threaded=True)
