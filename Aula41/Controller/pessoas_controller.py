from flask_restful import Resource
from Dao.pessoa_dao import PessoaDao
from flask import request
from model.pessoa_model import PessoaModel


class PessoaController(Resource):
    def __init__(self):
        self.dao = PessoaDao()

    def get(self, id=None):
        if id:
            return self.dao.get_by_id(id)
        return self.dao.list_all()

    def post(self):
        nome = request.json['nome']
        sobrenome = request.json['sobrenome']
        idade = int(request.json['idade'])
        pessoa = PessoaModel(nome, sobrenome, idade)
        return self.dao.insert(pessoa)

    def put(self, id):
        nome = request.json['nome']
        sobrenome = request.json['sobrenome']
        idade = int(request.json['idade'])
        pessoa = PessoaModel(nome, sobrenome, idade, id)
        return self.dao.update(pessoa)

    def delete(self, id):
        return self.dao.remove(id)