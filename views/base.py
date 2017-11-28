# -*- coding: utf-8 -*-
from app import app

from templates.home import HomePage, DoveSiamo, ChiSiamo, Galleria, Eventi, Contatti, Social

@app.route('/')
def index():
    return HomePage().render()


@app.route('/chi_siamo')
def chi_siamo():
    return ChiSiamo().render()


@app.route('/eventi')
def eventi():
    return Eventi().render()


@app.route('/galleria')
def galleria():
    return Galleria().render()


@app.route('/contatti')
def contatti():
    return Contatti().render()


@app.route('/dove_siamo')
def dove_siamo():
    return DoveSiamo().render()


@app.route('/social')
def social():
    return Social().render()
