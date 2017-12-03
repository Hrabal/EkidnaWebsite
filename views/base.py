# -*- coding: utf-8 -*-
import os
from flask import url_for
from facepy import GraphAPI

from config import oauth_access_token
from app import app

from templates.home import HomePage, DoveSiamo, ChiSiamo, Galleria, Eventi, Contatti, Rottura

@app.route('/')
def index():
    return HomePage().render()


@app.route('/chi_siamo')
def chi_siamo():
    files = os.listdir(os.path.join(app.static_folder, 'files', 'chisiamo'))
    return ChiSiamo(data={'files': files}).render()


@app.route('/eventi')
def eventi():
    graph = GraphAPI(oauth_access_token)
    events = graph.get('associazioneekidna/events')
    return Eventi(data={'events': events}).render()


@app.route('/galleria')
def galleria():
    pics = os.listdir(os.path.join(app.static_folder, 'img', 'gallery'))
    return Galleria(data={'pics': pics}).render()


@app.route('/contatti')
def contatti():
    return Contatti().render()


@app.route('/dove_siamo')
def dove_siamo():
    return DoveSiamo().render()


@app.route('/rottura_del_silenzio')
def rottura():
    locandine = os.listdir(os.path.join(app.static_folder, 'img', 'rottura'))
    return Rottura(data={'locandine': locandine}).render()
