# Aula 10 - 20-11-2019
#
#--- Web - Calculadora

nome_pagina = 'Calculadora'

from flask import Flask, render_template, request
from MetodosExercicio import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html',titulo=nome_pagina)

@app.route('/calcular')
def calcular():
    n1 = float(request.args['n1'])
    n2 = float(request.args['n2'])
    rsoma = soma(n1,n2)
    rsub = sub(n1,n2)
    rmult = mult(n1,n2)
    rdivfra = divfra(n1,n2)
    rdivint = divint(n1,n2)
    rrestodiv = restodiv(n1,n2)
    rraiz1 = raiz1(n1,n2)
    rraiz2 = raiz2(n1,n2)
    resultados = {'soma':rsoma,'sub':rsub,'mult':rmult,'divfra':rdivfra,'divint':rdivint,'restodiv':rrestodiv,'raiz1':rraiz1,'raiz2':rraiz2}
    
    return render_template('resultado.html', resultados = resultados, n1 = n1,n2 = n2)
    # return render_template('resultado.html',n1 = n1, n2 = n2, soma = rsoma, subtracao = rsub,multiplicacao = rmult,divisao_inteira = rdivint,divisao_fracionada = rdivfra,resto = rrestodiv,raiz1 = rraiz1,raiz2 = rraiz2)

app.run()