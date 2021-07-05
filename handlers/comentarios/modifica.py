#coding: utf-8
# Modifica Pelicula

import webapp2
import time

from webapp2_extras import jinja2
from model.comentario import Comentario

class ModificaComentarioHandler(webapp2.RequestHandler):

    def get(self):
        comentario = Comentario.recupera(self.request)
        valores_plantilla = {
            "pelicula_clave": self.request.GET["plc"],
            "comentario": comentario,
            "comentario_clave": self.request.GET["id"]
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("modifica_comentario.html",
                                                  **valores_plantilla))
    def post(self):
        str_puntuacion = self.request.get("edPuntuacion", "")
        opinion = self.request.get("edOpinion", "")
        pelicula_clave = self.request.GET["plc"]
        comentario = Comentario.recupera(self.request)

        try:
            puntuacion = int(str_puntuacion)
        except ValueError:
            puntuacion = -1

        if ( not(opinion) or not (str_puntuacion)):
            return self.redirect("comentarios/modifica?plc="+ pelicula_clave)
        else:
            comentario.puntuacion = puntuacion
            comentario.opinion = opinion
            comentario.put()
            time.sleep(1)
            return self.redirect("/comentarios/lista?plc=" + pelicula_clave)


app = webapp2.WSGIApplication([
    ('/comentarios/modifica', ModificaComentarioHandler)
], debug=True)