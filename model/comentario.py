#Comentario que pertenece a una pelicula

from google.appengine.ext import ndb

from pelicula import Pelicula

class Comentario(ndb.Model):
    hora = ndb.DateTimeProperty(auto_now_add=True)
    opinion = ndb.StringProperty(default="")
    puntuacion = ndb.IntegerProperty(required=True)
    pelicula_clave = ndb.KeyProperty(kind=Pelicula)

    @staticmethod
    def recupera_para(req):
        try:
            id_plc = req.GET["plc"]
        except KeyError:
            id_plc = ""

        if id_plc:
            pelicula_clave = ndb.Key(urlsafe=id_plc)
            comentarios = Comentario.query(Comentario.pelicula_clave==pelicula_clave)
            return (pelicula_clave.get(), comentarios)
        else:
            print("Error: pelicula no encontrada")

    @staticmethod
    def recupera(req):
        try:
            id = req.GET["id"]
        except:
            id = ""
        return ndb.Key(urlsafe=id).get()