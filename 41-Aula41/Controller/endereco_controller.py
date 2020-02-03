from flask_restful import Resource
from Dao.endereco_dao import EnderecoDao
from flask import request
from model.endereco_model import EnderecoModel


class EnderecoController(Resource):
    def __init__(self):
        self.dao = EnderecoDao()

    def get(self, id = None):
        if id:
            return self.dao.get_by_id(id)
        return self.dao.list_all()

    def post(self):
        logradoro = request.json['logradouro']
        numero = int(request.json['numero'])
        complemento = request.json['complemento']
        bairro = request.json['bairro']
        cidade = request.json['cidade']
        cep = request.json['cep']
        endereco = EnderecoModel(logradoro, numero, complemento, bairro, cidade, cep)
        return self.dao.insert(endereco)

    def put(self, id):
        logradoro = request.json['logradouro']
        numero = int(request.json['numero'])
        complemento = request.json['complemento']
        bairro = request.json['bairro']
        cidade = request.json['cidade']
        cep = request.json['cep']
        endereco = EnderecoModel(logradoro, numero, complemento, bairro, cidade, cep, id)
        return self.dao.update(endereco)

    def delete(self, id):
        return self.dao.remove(id)