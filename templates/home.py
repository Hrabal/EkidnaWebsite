# -*- coding: utf-8 -*-
import arrow
from operator import itemgetter
from flask import url_for, g
from tempy.tempy import Escaped
from tempy.tags import Div, Img, Link, Script, H2, Meta, Center, Br, A, Pre, Blockquote
from tempy.elements import Css
from tempy.widgets import TempyPage

base_keywords = ['ekdina', 'musica', 'carpi', 'centro sociale', 'live', ]
content = 'Ekdina'


class GoogleAnalizzabile:
    def _get_analytics(self):
        return [Script(async=True, src="https://www.googletagmanager.com/gtag/js?id=UA-110964364-1"),
                Script()(Escaped("""window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'UA-110964364-1');"""))
                ]


class HomePage(TempyPage, GoogleAnalizzabile):
    def js(self):
        return [
            Script(src="https://code.jquery.com/jquery-3.2.1.min.js", crossorigin="anonymous"),
            Script(src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.3/umd/popper.min.js", integrity="sha384-vFJXuSJphROIrBnz7yo7oB41mKfc8JzQZiCq4NCceLEaO4IHwicKwpJf9c9IpFgh", crossorigin="anonymous"),
            Script(src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/js/bootstrap.min.js", integrity="sha384-alpBpkh1PFOepccYVYDB4do5UnbKysX5WZXm3XxPqe5iKTfUKjNkCk9SaVuEZflJ", crossorigin="anonymous"),
            Script(src=url_for('static', filename='js/main.js')),
        ]

    def css(self):
        return [
            Link(href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css", rel="stylesheet", integrity="sha384-PsH8R72JQ3SOdhVi3uxftmaW6Vc51MKb0q5P2rRUpPvrszuE4W1povHYgTpBfshb", crossorigin="anonymous"),
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
        self.head(Meta(charset="utf-8"), Meta(name="viewport", content="width=device-width, initial-scale=1, shrink-to-fit=no",))
        self.head.title(self.default_init['title'])
        self.body(
            Div(id='bg')(Img(src=url_for('static', filename='img/bg.jpg'))),
            Div(klass='container')(
                Div(id='title', klass='row no-gutters align-items-end justify-content-around')(
                    Div(klass='col-md bigLetter')('E', Div(klass='menuItem', link="/chi_siamo")('Chi Siamo')),
                    Div(klass='col-md bigLetter')('k', Div(klass='menuItem', link="/eventi")('Eventi')),
                    Div(klass='col-md bigLetter')('i', Div(klass='menuItem', link="/galleria")('Galleria')),
                    Div(klass='col-md bigLetter')('d', Div(klass='menuItem', link="/contatti")('Contatti')),
                    Div(klass='col-md bigLetter')('n', Div(klass='menuItem', link="/dove_siamo")('Dove Siamo')),
                    Div(klass='col-md bigLetter')('a', Div(klass='menuItem', link="/rottura_del_silenzio")('Rottura Del Silenzio')),
                ),
                Div(id='content_container', klass='row no-gutters align-items-start justify-content-center content_container')(Div(id='content', klass="col-md")(
                    self._get_analytics()
                  ))
            )
        )




class DoveSiamo(Div, GoogleAnalizzabile):
    def init(self):
        self(
            Center()(H2()('Via Livorno 9, 41012 Carpi (MO)')),
            Div(id='map_container')(
                Meta(name="viewport", content="initial-scale=1.0, user-scalable=no"),
                Meta(charset="utf-8"),
                Css({'#map': {'height': '62vh', "box-sizing": "content-box"}}),
                Div(id='map'),
                Script(src=url_for('static', filename='js/gmap.js'))(),
                Script(src="https://maps.googleapis.com/maps/api/js?key=AIzaSyCE74FjhQ39oEwV9kuBI8qedSFOKBWypyQ&callback=initMap", async=bool, defer=bool)
            )
        )


class ChiSiamo(Div, GoogleAnalizzabile):
    def init(self):
        self(
            Center()(Img(src=url_for('static', filename='img/ekidna.png'))), Br(),
            Div(klass='pageTitle')(Center()('Chi Siamo')),
            Pre(klass='preText')("""Fondata nel 1998, l'Associazione Culturale Ekidna si occupa di costruire uno spazio/cantiere aperto alle realtà culturali ed artistiche della zona (ma non solo) che necessitano di spazi di creazione e di visibilità, in un sistema che tende a schiacciare e a rendere pressocchè invisibile tutto ciò che non è commerciabile con alto profitto.

Nel 2002 il progetto si è concretizzato nelle Ex-Scuole Ernesta Bertesi, di San Martino sul Secchia (nelle campagne carpigiane), concesse in comodato d'uso dal Comune di Carpi, dopo lunghe vicissitudini burocratiche.

La struttura fu consegnata in stato di totale abbandono e, da allora, la scelta di Ekidna è stata quella di fornire lavoro volontario ed investire i proventi delle iniziative nella ristrutturazione dello stabile, perchè i progetti artistici possano avere un luogo dove nascere e crescere.

Ekidna è un centro autogestito, completamente slegato da qualsiasi partito o potere politico, che deve quindi auto-finanziarsi completamente, con iniziative di vario genere, legate alle varie discipline artistiche e ad attività culturali."""),
        )
        self(Div(klass='pdf')(A(target='_blank', href=url_for('static', filename='files/chisiamo/%s' % file))(Img(klass='socialIcon', src=url_for('static', filename='img/pdf.png')), file.title()[:-4])) for file in self._data['files'])
        self(self._get_analytics())


class Galleria(Div, GoogleAnalizzabile):
    def init(self):
        self(Div(klass='pageTitle')('Galleria'))
        self(Div(id='photos')(
                Img(src=url_for('static', filename='img/gallery/%s' % pic)) for pic in self._data.get('pics',[])
            )
        )
        self(self._get_analytics())


class Eventi(Div, GoogleAnalizzabile):
    def init(self):
        self(Div(klass='pageTitle')('Eventi'))
        for event in sorted(self._data['events']['data'], key=itemgetter('start_time'), reverse=True):
            self(
                Div(klass='event')(
                    Div(klass='eventDate')(arrow.get(event['start_time']).strftime('%d-%m-%Y')), Div(klass="eventTitle")(event['name']), Pre(klass="preText")(event['description']))
            )
        self(self._get_analytics())


class Contatti(Div, GoogleAnalizzabile):
    def init(self):
        self(Div(klass='pageTitle')('Contatti'))
        self(
            "Ekidna è uno spazio aperto ad ogni proposta, se hai una band e ti piacerebbe suonare da noi, se sei un'agenzia e vuoi proporci il tuo rooster, se hai un'idea che vorresti realizzare in Ekidna, scrivici!", Br(),
            "Cerchiamo di rispondere a tutti, e di dare spazio a tutti.", Br(),
            "Scrivici a ", A(href='mailto:ekidnacarpi@gmail.com')('ekidnacarpi@gmail.com'), Br(),
            "Oppure su ", A(href='http://www.facebook.com/associazioneekidna')('Facebook'), Br(),
            "Ma il modo migliore per proporci qualcosa è (se sei della zona) venire alle nostre riunioni settimanali (di solito il martedì, ma può variare)"
        )
        self(Div(klass='pageTitle')('Social'))
        self(
            Img(klass='socialIcon', src=url_for('static', filename='img/social/facebook.png')), A(href='http://www.facebook.com/associazioneekidna')('Facebook'),
            Img(klass='socialIcon', src=url_for('static', filename='img/social/blogspot.png')), A(href='http://associazioneekidna.blogspot.it/')('Blogspot'),
            Img(klass='socialIcon', src=url_for('static', filename='img/social/twitter.png')), A(href='http://twitter.com/ekidnacarpi')('Twitter'),
            Img(klass='socialIcon', src=url_for('static', filename='img/social/youtube.png')), A(href='http://www.youtube.com/channel/UC9URlWUKYelFlTBrFvc7Nyw')('YouTube'),
        )
        self(self._get_analytics())


class Rottura(Div, GoogleAnalizzabile):
    def init(self):
        self(Div(klass='pageTitle')('Rottura Del Silenzio'))
        self(
            Pre(klass='preText')("""
Dal 1998 Associazione Ekidna organizza la Rottura Del Silenzio, un festival diy (do it yourself).
Dopo 20 anni non sappiamo più cosa dire per raccontarla, quindi lo lasciamo fare agli altri:"""
            ),
            Blockquote()(Pre(klass='preText')("""Succede che in Emilia, qui dalle nostre parti, finita la primavera, ci viene una certa voglia di stare seduti su un prato tutti rivolti verso un palco, con uno sguazzone  in mano (acqua frizzante con vino bianco scadente), andando a tempo di musica con la testa. Il bello di queste cose è che iniziano al venerdì sera e vanno avanti fino alla domenica. Un’altra cosa bella è che solitamente si entra a offerta libera;: lasci quello che vuoi, se lo vuoi.

Entri in questi posti e sei circondato tutto il giorno dalla musica di gruppi di cui non conosci manco il nome ma dentro di te pensi: “Cazzo! Questi spaccano!” e avvicinandoti ad una tizia chiedi il nome di chi ha appena suonato così te li puoi andare a riascoltare su Spotify, scoprendo poi che sono meglio dal vivo. Ti chiedi anche se la conversazione con la tizia citata sopra avrà un epilogo felice, ma scopri con grosso dispiacere che è lesbica e che quindi, forse, è meglio tornare con i tuoi amici a fumare e a prendere l’ennesimo sguazzone. Girando scopri anche che ci sono un sacco di banchetti. Ce n’è uno di un’etichetta indipendente che crede ancora nel fare musica DOITYOURSELF, come dovrebbe essere. Poi ce n’è un altro di una rivista, che stampa giornaletti e li dà via a gratis! Cioè veramente, tu puoi prenderne quanti ne vuoi, per amici, parenti, morose, basta che si leggano. Guarda questi! Scrivono per il puro piacere di scrivere, per il puro piacere di raccontare. Sempre DOITYOURSELF, sia chiaro! Poi ce n’è un altro che vende braccialetti DOITYOURSELF di cui sicuramente la tua ex-morosa fricchettona-ma-anche-no, ne sarebbe stata entusiasta. Poi ragioni un po’ sul DOITYOURSELF, ma veramente questa gente si sbatte per fare qualcosa? Ti guardi intorno e vedi che sono tutti felici e sorridenti, come dovrebbe essere. Capisci che queste persone si sbattono perchè lo vogliono, per l’amore di fare, per lo stare insieme, per la musica e per divertirsi. E pensi che questo posto è proprio un bel posto.

Uno di questi si chiama Ekidna, un circolo alle porte di Carpi (San Martino Scuole), a cui piace molto fare le cose (e le fanno veramente bene). In estate organizza questo festival che si chiama ROTTURA DEL SILENZIO; ora mai sono arrivati alla diciannovesima edizione. Quest’anno si svolgerà il 17-18-19 giugno e noi di Mumble: siamo felicissimi di farne parte. Per tutti i tre giorni ci suoneranno un sacco di gruppi, banchetti, cibo e sguazzoni. Il tutto è ad offerta libera e consigliamo veramente la presenza, non per tutte le cose citate sopra, ma perchè, in realtà, questi ragazzi hanno un Idromele (DOITYOURSELF) che è la fine del mondo."""
            )),
            "Giacomo Malaguti - ", A(href="http://www.mumbleduepunti.it/")('MUMBLE:'), Br(), Br(),
            "Per proporvi con banchetti, per dare una mano, per seperne qualcosa di più o solo per dire che ti piace: ", A(href="https://www.facebook.com/rotturadelsilenzio/")('facebook.com/rotturadelsilenzio')
        )
        self(Br(), Br())
        self(Div(id='photos')(
                Img(src=url_for('static', filename='img/rottura/%s' % pic)) for pic in sorted(self._data.get('locandine',[]), reverse=True)
            )
        )
        self(self._get_analytics())
