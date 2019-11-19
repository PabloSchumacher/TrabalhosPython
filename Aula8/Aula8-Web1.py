# Aula 8 - 18-11-2019
# web

from flask import Flask

app = Flask(__name__)
@app.route('/')
def inicio():
    return 'Bem vindos ao mundo real meus quiridus'

app.run()