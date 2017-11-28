# -*- coding: utf-8 -*-
from flask import url_for, g
from tempy.tags import Div, Img, Link, Script
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
            Link(href='https://fonts.googleapis.com/css?family=Source+Code+Pro:700', rel="stylesheet"),
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
                    Div(klass='bigLetter')('E', Div(klass='menuItem')('Chi Siamo')),
                    Div(klass='bigLetter')('k', Div(klass='menuItem')('Eventi')),
                    Div(klass='bigLetter')('i', Div(klass='menuItem')('Galleria')),
                    Div(klass='bigLetter')('d', Div(klass='menuItem')('Contatti')),
                    Div(klass='bigLetter')('n', Div(klass='menuItem')('Dove Siamo')),
                    Div(klass='bigLetter')('a', Div(klass='menuItem')('Social')),
                ),
                Div(id='content_container')(Div(id='content'))
            )
        )
