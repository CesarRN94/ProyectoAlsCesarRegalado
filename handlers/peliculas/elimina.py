#coding: utf-8
# Eliminar Pelicula

import webapp2
import time

from webapp2_extras import jinja2
from model.pelicula import Pelicula

class EliminaPeliculaHandler(webapp2.RequestHandler):
    def get(self):
        pelicula = Pelicula.recupera(self.request)
        pelicula.key.delete()
        time.sleep(1)
        return self.redirect("/")

app = webapp2.WSGIApplication([
    ('/peliculas/elimina', EliminaPeliculaHandler)
], debug=True)