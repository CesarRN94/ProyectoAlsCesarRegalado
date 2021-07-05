#!/usr/bin/env python
#coding: utf-8
#
# Copyright 2007 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from webapp2_extras import jinja2
from webapp2_extras.users import users

from model.comentario import Comentario
from model.pelicula import Pelicula

class ListaComentariosHandler(webapp2.RequestHandler):
    def get(self):
        pelicula, comentarios = Comentario.recupera_para(self.request)
        usr = users.get_current_user()

        if usr:
            url_usr = users.create_logout_url("/")
        else:
            url_usr = users.create_login_url("/")

        if users.is_current_user_admin():
            admin = True
        else:
            admin = False


        valores_plantilla = {

            "pelicula": pelicula,
            "comentarios": comentarios,
            "usr": usr,
            "url_usr": url_usr,
            "admin": admin
            }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("lista_comentarios.html",
                                                  **valores_plantilla))

app = webapp2.WSGIApplication([
    ('/comentarios/lista', ListaComentariosHandler)
], debug=True)
