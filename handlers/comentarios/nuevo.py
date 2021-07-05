#coding: utf-8
# Nuevo Comentario

import webapp2
import time

from webapp2_extras import jinja2
from google.appengine.ext import ndb

from model.comentario import Comentario

class NuevoComentarioHandler(webapp2.RequestHandler):
    def get(self):
        valores_plantilla = {

            "pelicula_clave": self.request.GET["plc"]

        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("nuevo_comentario.html",
                                                  **valores_plantilla))
    def post(self):
        opinion = self.request.get("edOpinion", "")
        str_puntuacion = self.request.get("edPuntuacion", "")
        pelicula_clave = self.request.GET["plc"]

        try:
            puntuacion = int(str_puntuacion)
        except ValueError:
            puntuacion = -1

        if ( puntuacion < 0
             or not(opinion)):
            return self.redirect("/")
        else:
            comentario = Comentario(opinion=opinion, puntuacion=puntuacion,
                                    pelicula_clave=ndb.Key(urlsafe=pelicula_clave))
            comentario.put()
            time.sleep(1)
            return self.redirect("/comentarios/lista?plc=" + pelicula_clave)


app = webapp2.WSGIApplication([
    ('/comentarios/nuevo', NuevoComentarioHandler)
], debug=True)

