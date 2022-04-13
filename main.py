from bottle import route, run
from helpers import somme
import sys


@route("/add/<a>/<b>")
def addition(a, b):
    return somme(a, b)


run(host="0.0.0.0", port=sys.argv[1], reloader=True)
