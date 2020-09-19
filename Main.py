#importando as Bibliotecas utilizadas na Aplicação
import os
from flask import Flask, jsonify
from flask_cors import CORS
from math import sqrt

app = Flask(__name__)

CORS(app)


# Fazendo Validação caso de erro apresenta o código ASCII
app.config['JSON_AS_ASCII'] = False



#Criando as Rotas da Aplicação
@app.route('/')
def root():
    return 'Seja Bem Vindo(a) <br> Digite qual operação gostaria de fazer entre as opções <br> <br>' + \
           '1 -  ' 'https://dsdtrabalho-andredelcole.herokuapp.com/add/firtsvalue/secondvalue <br>' + \
           '2 -  ' 'https://dsdtrabalho-andredelcole.herokuapp.com/subtraction/firtsvalue/secondvalue <br>' + \
           '3 -  ' 'https://dsdtrabalho-andredelcole.herokuapp.com/division/firtsvalue/secondvalue <br>' + \
           '4 -  ' 'https://dsdtrabalho-andredelcole.herokuapp.com/multiplication/firtsvalue/secondvalue <br>' + \
           '5 -  ' 'https://dsdtrabalho-andredelcole.herokuapp.com/squareroot/value <br>' + \
           '6 -  ' 'https://dsdtrabalho-andredelcole.herokuapp.com/power/base/exponent <br>' + \
           '7 -  ' 'https://dsdtrabalho-andredelcole.herokuapp.com/arithmeticaverage/primeirovalor;segundo;terceiro;... <br>' + \
           '8 -  ' 'https://dsdtrabalho-andredelcole.herokuapp.com/harmonicmean/primeirovalor;segundo;terceiro;... <br>' + \
           '9 -  ' 'https://dsdtrabalho-andredelcole.herokuapp.com/mod/primeirovalor;segundo;terceiro;... <br>' + \  
                      'Obrigado por Utilizar a API de Consulta'




#Rota Somar
@app.route('/add/<value1>/<value2>', methods=['GET'])
def add(value1, value2):

    try:
        value1 = int(value1)
    except:
        return 'Seu primeiro Valor Digitado está Incorreto, digite um valor valido.'

    try:
        value2 = int(value2)
    except:
        return 'Seu segundo Valor Digitado está Incorreto, digite um valor valido.'

    result = {"Resultado": value1 + value2}

    return jsonify(result)




#Rota Subtração
@app.route('/subtraction/<value1>/<value2>', methods=['GET'])
def subtraction(value1, value2):
    try:
        value1 = int(value1)
    except:
        return 'Seu primeiro Valor Digitado está Incorreto, digite um valor valido.'

    try:
        value2 = int(value2)
    except:
        return 'Seu segundo Valor Digitado está Incorreto, digite um valor valido.'

    result = {"Resultado": value1 - value2}

    return jsonify(result)




#Rota Divisão
@app.route('/division/<value1>/<value2>', methods=['GET'])
def division(value1, value2):
    try:
        value1 = int(value1)
    except:
        return 'Seu primeiro Valor Digitado está Incorreto, digite um valor valido.'

    try:
        value2 = int(value2)
    except:
        return 'Seu segundo Valor Digitado está Incorreto, digite um valor valido.'

    try:
        result = {"Resultado": value1 / value2}
    except ZeroDivisionError:
        return 'Você não pode realizar uma Divisão por zero, verifique os números e tente novamente'

    return jsonify(result)




#Rota Multiplicação
@app.route('/multiplication/<value1>/<value2>', methods=['GET'])
def multiplication(value1, value2):
    try:
        value1 = int(value1)
    except:
        return 'Seu primeiro Valor Digitado está Incorreto, digite um valor valido.'

    try:
        value2 = int(value2)
    except:
        return 'Seu segundo Valor Digitado está Incorreto, digite um valor valido.'

    result = {"Resultado": value1 * value2}

    return jsonify(result)





@app.route('/squareroot/<value>', methods=['GET'])
def squareroot(value):
    try:
        valor1 = int(value)
    except:
        return 'Valor inválido.'

    ret = {"Resultado": sqrt(valor1)}

    return jsonify(ret)


# ----------------------------------------------------------------------------------------------------------------------


@app.route('/power/<base>/<exponent>', methods=['GET'])
def power(base, exponent):
    try:
        li_base = int(base)
    except:
        return 'Base Inválida.'

    try:
        li_exponent = int(exponent)
    except:
        return 'Expoente inválido.'

    ret = {"Resultado": li_base ** li_exponent}

    return jsonify(ret)


# ----------------------------------------------------------------------------------------------------------------------


@app.route('/arithmeticaverage/<value1>', methods=['GET'])
def arithmeticaverage(value1):

    try:
        array = [int(numeros) for numeros in value1.split(';')]
    except:
        return 'A sequencia não possui somente números'

    ret = {"Resultado": sum(array) / len(array)}

    return jsonify(ret)


# ----------------------------------------------------------------------------------------------------------------------


@app.route('/harmonicmean/<value1>', methods=['GET'])
def harmonicmean(value1):

    try:
        array = [1 / int(numeros) for numeros in value1.split(';')]
    except:
        return 'A sequencia não possui somente números'


    ret = {"Resultado": len(array) / sum(array)}

    return jsonify(ret)


# ----------------------------------------------------------------------------------------------------------------------


@app.route('/mod/<value1>', methods=['GET'])
def mod(value1):

    dicionario = {}

    try:
        array = [int(numeros) for numeros in value1.split(';')]
    except:
        return 'A sequencia não possui somente números'

    for numeros in array:
        try:
            dicionario[numeros] = dicionario[numeros] + 1
        except:
            dicionario[numeros] = 1

    ret = {"Resultado": [numero for numero, repeticoes in dicionario.items() if repeticoes == max(dicionario.values())]}

    return jsonify(ret)


def main():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


if __name__ == "__main__":
    main()
