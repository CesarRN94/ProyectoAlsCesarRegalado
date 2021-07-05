#coding: utf-8
# Modifica Pelicula

import webapp2
import time

from webapp2_extras import jinja2
from model.pelicula import Pelicula

class ModificaPeliculaHandler(webapp2.RequestHandler):

    def get(self):
        pelicula = Pelicula.recupera(self.request)
        valores_plantilla = {
            "pelicula": pelicula,
            "pelicula_clave": self.request.GET["id"]
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("modifica_pelicula.html",
                                                  **valores_plantilla))
    def post(self):
        titulo = self.request.get("edTitulo", "")
        sinopsis = self.request.get("edSinopsis", "")
        str_puntuacion = self.request.get("edPuntuacion", "")
        pelicula = Pelicula.recupera(self.request)

        try:
            puntuacion = int(str_puntuacion)
        except ValueError:
            puntuacion = -1

        if ( puntuacion < 0 or not(titulo) or not (sinopsis)):
            return self.redirect("peliculas/modifica")
        else:
            pelicula.titulo = titulo
            pelicula.sinopsis = sinopsis
            pelicula.puntuacion = puntuacion
            pelicula.put()
            time.sleep(1)
            return self.redirect("/")


app = webapp2.WSGIApplication([
    ('/peliculas/modifica', ModificaPeliculaHandler)
], debug=True)