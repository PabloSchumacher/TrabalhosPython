# Aula 9 - 19-11-2019
# web

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicia():
    return render_template('inicio.html')

app.run()