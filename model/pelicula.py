

from google.appengine.ext import ndb

class Pelicula(ndb.Model):
    titulo = ndb.StringProperty(indexed=True)
    sinopsis = ndb.StringProperty(required=True)
    puntuacion = ndb.IntegerProperty(required=True)

    @staticmethod
    def recupera(req):
        try:
            id = req.GET["id"]
        except KeyError:
            id = ""

        return ndb.Key(urlsafe=id).get()
