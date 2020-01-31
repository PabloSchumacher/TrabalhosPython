from flask import Flask
from flask_restful import Api
from Controller.pessoas_controller import PessoaController

app = Flask(__name__)
api = Api(app)

api.add_resource(PessoaController, '/api/pessoas')

@app.route('/')
def index():
    return 'Bem-Vindo a API'

app.run(debug=True, port=80)