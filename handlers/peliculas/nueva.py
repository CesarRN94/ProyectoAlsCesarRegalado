#coding: utf-8
# Nueva Pelicula

import webapp2
import time

from webapp2_extras import jinja2
from model.pelicula import Pelicula

class NuevaPeliculaHandler(webapp2.RequestHandler):

    def get(self):
        valores_plantilla = {

        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("nueva_pelicula.html",
                                                  **valores_plantilla))
    def post(self):
        titulo = self.request.get("edTitulo", "")
        str_puntuacion = self.request.get("edPuntuacion", "")
        sinopsis = self.request.get("edSinopsis", "")

        try:
            puntuacion = int(str_puntuacion)
        except ValueError:
            puntuacion = -1

        if ( puntuacion < 0 or not(titulo) or not (sinopsis)):
            return self.redirect("/")
        else:
            pelicula = Pelicula(titulo=titulo, puntuacion=puntuacion,
                                sinopsis=sinopsis)
            pelicula.put()
            time.sleep(1)
            return self.redirect("/")


app = webapp2.WSGIApplication([
    ('/peliculas/nueva', NuevaPeliculaHandler)
], debug=True)

