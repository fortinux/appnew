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
def index():
    return "<H1>Hola Mundo!</H1>"
