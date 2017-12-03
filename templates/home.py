# -*- coding: utf-8 -*-
import arrow
from operator import itemgetter
from flask import url_for, g
from tempy.tags import Div, Img, Link, Script, H2, Meta, Center, Br, A, Pre, Blockquote
from tempy.elements import Css
from tempy.widgets import TempyPage

base_keywords = ['ekdina', 'musica', 'carpi', 'centro sociale', 'live', ]
content = 'Ekdina'


class HomePage(TempyPage):
    def js(self):
        return [
            Script(src="//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"),
            Script(src=url_for('static', filename='js/main.js')),
        ]

    def css(self):
        return [
            Link(href=url_for('static', filename='css/style.css'), rel="stylesheet", typ="text/css"),
            Link(href='https://fonts.googleapis.com/css?family=Montserrat|Source+Code+Pro:700', rel="stylesheet"),
        ]

    default_init = {
        'title': 'Associazione EcoCulturale Ekidna',
        'content': content,
        'keywords': base_keywords
    }

    def init(self):
        self.head(self.css(), self.js())
        self.head.title(self.default_init['title'])
        self.body(
            Div(id='bg')(Img(src=url_for('static', filename='img/bg.jpg'))),
            Div(id='container')(
                Div(id='title')(
                    Div(klass='bigLetter')('E', Div(klass='menuItem', link="/chi_siamo")('Chi Siamo')),
                    Div(klass='bigLetter')('k', Div(klass='menuItem', link="/eventi")('Eventi')),
                    Div(klass='bigLetter')('i', Div(klass='menuItem', link="/galleria")('Galleria')),
                    Div(klass='bigLetter')('d', Div(klass='menuItem', link="/contatti")('Contatti')),
                    Div(klass='bigLetter')('n', Div(klass='menuItem', link="/dove_siamo")('Dove Siamo')),
                    Div(klass='bigLetter')('a', Div(klass='menuItem', link="/social")('Social')),
                ),
                Div(id='content_container')(Div(id='content'))
            )
        )


class DoveSiamo(Div):
    def init(self):
        self(
            Center()(H2()('Via Livorno 9, 41012 Carpi (MO)')),
            Div(id='map_container')(
                Meta(name="viewport", content="initial-scale=1.0, user-scalable=no"),
                Meta(charset="utf-8"),
                Css({'#map': {'height': '62vh'}}),
                Div(id='map'),
                Script(src=url_for('static', filename='js/gmap.js'))(),
                Script(src="https://maps.googleapis.com/maps/api/js?key=AIzaSyCE74FjhQ39oEwV9kuBI8qedSFOKBWypyQ&callback=initMap", async=bool, defer=bool)
            )
        )


class ChiSiamo(Div):
    def init(self):
        self(
            Center()(Img(src=url_for('static', filename='img/ekidna.png'))), Br(),
            "Fondata nel 1998, l'Associazione Culturale Ekidna si occupa di costruire uno spazio/cantiere aperto alle realtà culturali ed artistiche della zona (ma non solo) che necessitano di spazi di creazione e di visibilità, in un sistema che tende a schiacciare e a rendere pressocchè invisibile tutto ciò che non è commerciabile con alto profitto.", Br(), Br(),
            "Nel 2002 il progetto si è concretizzato nelle Ex-Scuole Ernesta Bertesi, di San Martino sul Secchia (nelle campagne carpigiane), concesse in comodato d'uso dal Comune di Carpi, dopo lunghe vicissitudini burocratiche.", Br(), Br(),
            "La struttura fu consegnata in stato di totale abbandono e, da allora, la scelta di Ekidna è stata quella di fornire lavoro volontario ed investire i proventi delle iniziative nella ristrutturazione dello stabile, perchè i progetti artistici possano avere un luogo dove nascere e crescere.", Br(), Br(),
            "Ekidna è un centro autogestito, completamente slegato da qualsiasi partito o potere politico, che deve quindi auto-finanziarsi completamente, con iniziative di vario genere, legate alle varie discipline artistiche e ad attività culturali.", Br(), Br(),
        )


class Galleria(Div):
    def init(self):
        self(Div(klass='pageTitle')('Galleria'))
        self(Div(id='photos')(
                Img(src=url_for('static', filename=f'img/gallery/{pic}')) for pic in self._data.get('pics',[])
            )
        )


class Eventi(Div):
    def init(self):
        self(Div(klass='pageTitle')('Eventi'))
        for event in sorted(self._data['events']['data'], key=itemgetter('start_time'), reverse=True):
            self(
                Div(klass='event')(
                    Div(klass='eventDate')(arrow.get(event['start_time']).strftime('%d-%m-%Y')), Div(klass="eventTitle")(event['name']), Pre(klass="preText")(event['description']))
            )


class Contatti(Div):
    def init(self):
        self(
            "Per contattarci scrivici a ", A(href='mailto:ekidnacarpi@gmail.com')('ekidnacarpi@gmail.com'), Br(),
            "Oppure scrivici su ", A(href='http://www.facebook.com/associazioneekidna')('Facebook'), Br(),
            "Oppure vieni alle nostre riunioni settimanali (di solito il martedì, ma chiedere è meglio che star lì al freddo!)"
        )


class Social(Div):
    def init(self):
        self(
            H2()('facebook - ', A(href='http://www.facebook.com/associazioneekidna')('http://www.facebook.com/associazioneekidna')),
            H2()('blogspot - ', A(href='http://associazioneekidna.blogspot.it/')('http://associazioneekidna.blogspot.it/')),
            H2()('twitter - ', A(href='http://twitter.com/ekidnacarpi')('http://twitter.com/ekidnacarpi')),
            H2()('youtube - ', A(href='http://www.youtube.com/channel/UC9URlWUKYelFlTBrFvc7Nyw')('http://www.youtube.com/channel/UC9URlWUKYelFlTBrFvc7Nyw')),
        )
