#!/user/bin/env python3
"""
[Add module documentation here]

Author: Fortinux
info@fortinux.com
Date: [Add date here]
"""
from flask import Flask


app = Flask(__name__)


@app.route("/")
def home():
    return "<H1>Esta es la página principal</H1>"


@app.route("/servicios")
def servicios():
    return "<H1>Esta es la página de servicios</H1>"


@app.route("/contacto")
def contacto():
    return "<H1>Esta es la página de contacto</H1>"


@app.route("/admin")
def admin():
    return "<H1>Esta es la página de admin</H1>"
