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
    return 'Seja Bem Vindo(a)<br><br> API CALCULATOR <br><br> Digite qual operação gostaria de fazer entre as opções <br> <br>' + \
           '1 -  ' 'https://dsdtrabalho-andredelcole.herokuapp.com/add/firtsvalue/secondvalue <br>' + \
           '2 -  ' 'https://dsdtrabalho-andredelcole.herokuapp.com/subtraction/firtsvalue/secondvalue <br>' + \
           '3 -  ' 'https://dsdtrabalho-andredelcole.herokuapp.com/division/firtsvalue/secondvalue <br>' + \
           '4 -  ' 'https://dsdtrabalho-andredelcole.herokuapp.com/multiplication/firtsvalue/secondvalue <br>' + \
           '5 -  ' 'https://dsdtrabalho-andredelcole.herokuapp.com/squareroot/value <br>' + \
           '6 -  ' 'https://dsdtrabalho-andredelcole.herokuapp.com/power/base/exponent <br>' + \
           '7 -  ' 'https://dsdtrabalho-andredelcole.herokuapp.com/arithmeticaverage/firtsvalue;second;third;... <br>' + \
           '8 -  ' 'https://dsdtrabalho-andredelcole.herokuapp.com/harmonicmean/firtsvalue;second;third;... <br>' + \
           '9 -  ' 'https://dsdtrabalho-andredelcole.herokuapp.com/mod/firtsvalue;second;third;... <br> <br> <br>'   
                    #'Obrigado por Utilizar a API Calculator'




#Rota Somar
@app.route('/add/<value1>/<value2>', methods=['GET'])
def add(value1, value2):

    try:
        value1 = int(value1)
    except:
        return 'Seu primeiro valor digitado está incorreto, digite um valor valido.'

    try:
        value2 = int(value2)
    except:
        return 'Seu segundo valor digitado está incorreto, digite um valor valido.'

    result = {"Resultado": value1 + value2}

    return jsonify(result)




#Rota Subtração
@app.route('/subtraction/<value1>/<value2>', methods=['GET'])
def subtraction(value1, value2):
    try:
        value1 = int(value1)
    except:
        return 'Seu primeiro valor digitado está incorreto, digite um valor valido.'

    try:
        value2 = int(value2)
    except:
        return 'Seu segundo valor digitado está incorreto, digite um valor valido.'

    result = {"Resultado": value1 - value2}

    return jsonify(result)




#Rota Divisão
@app.route('/division/<value1>/<value2>', methods=['GET'])
def division(value1, value2):
    try:
        value1 = int(value1)
    except:
        return 'Seu primeiro valor digitado está incorreto, digite um valor valido.'

    try:
        value2 = int(value2)
    except:
        return 'Seu segundo valor digitado está incorreto, digite um valor valido.'

    try:
        result = {"Resultado": value1 / value2}
    except ZeroDivisionError:
        return 'Você não pode realizar uma divisão por zero, verifique os números e tente novamente'

    return jsonify(result)




#Rota Multiplicação
@app.route('/multiplication/<value1>/<value2>', methods=['GET'])
def multiplication(value1, value2):
    try:
        value1 = int(value1)
    except:
        return 'Seu primeiro valor digitado está incorreto, digite um valor valido.'

    try:
        value2 = int(value2)
    except:
        return 'Seu segundo valor digitado está incorreto, digite um valor valido.'

    result = {"Resultado": value1 * value2}

    return jsonify(result)




#Rota Raiz Quadrada
@app.route('/squareroot/<value>', methods=['GET'])
def squareroot(value):
    try:
        value1 = int(value)
    except:
        return 'O valor digitado é inválido, digite um valor correto.'

    result = {"Resultado": sqrt(value1)}

    return jsonify(result)



#Rota da Potenciação
@app.route('/power/<base>/<exponent>', methods=['GET'])
def power(base, exponent):
    try:
        vl_base = int(base)
    except:
        return 'O valor para a base está inválido, digite um valor correto.'

    try:
        vl_exponent = int(exponent)
    except:
        return 'Expoente inválido.'

    result = {"Resultado": vl_base ** vl_exponent}

    return jsonify(result)




#Rota Média Aritimetica
@app.route('/arithmeticaverage/<value1>', methods=['GET'])
def arithmeticaverage(value1):

    try:
        array = [float(numbers) for numbers in value1.split(';')]
    except:
        return 'A sequencia digitada deve possuir somente números'

    result = {"Resultado": sum(array) / len(array)}

    return jsonify(result)




#Rota da Média Harmonica
@app.route('/harmonicmean/<value1>', methods=['GET'])
def harmonicmean(value1):

    try:
        array = [1 / float(numbers) for numbers in value1.split(';')]
    except:
        return 'A sequencia digitada deve possuir somente números'


    result = {"Resultado": len(array) / sum(array)}

    return jsonify(result)




#Rota da Moda
@app.route('/mod/<value1>', methods=['GET'])
def mod(value1):

    dicionario = {}

    try:
        array = [int(numbers) for numbers in value1.split(';')]
    except:
        return 'A sequencia digitada deve possuir somente números'

    for numbers in array:
        try:
            dicionario[numbers] = dicionario[numbers] + 1
        except:
            dicionario[numbers] = 1

    result = {"Resultado": [numbers for numbers, repeticoes in dicionario.items() if repeticoes == max(dicionario.values())]}

    return jsonify(result)


def main():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


if __name__ == "__main__":
    main()
