# -*- coding: utf-8 -*-
from app import app

from templates.home import HomePage

@app.route('/')
def index():
    return HomePage().render()
