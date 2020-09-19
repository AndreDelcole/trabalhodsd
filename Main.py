import os
from flask import Flask, jsonify
from flask_cors import CORS
from math import sqrt

app = Flask(__name__)

CORS(app)

app.config['JSON_AS_ASCII'] = False

# ----------------------------------------------------------------------------------------------------------------------


@app.route('/')
def root():
    return 'Digite qual operação gostaria de fazer entre as opções <br> <br>' + \
           'https://trab-robson-wallace-d27hec6.herokuapp.com/sum/primeirovalor/segundovalor <br>' + \
           'https://trab-robson-wallace-d27hec6.herokuapp.com/subtraction/primeirovalor/segundovalor <br>' + \
           'https://trab-robson-wallace-d27hec6.herokuapp.com/division/primeirovalor/segundovalor <br>' + \
           'https://trab-robson-wallace-d27hec6.herokuapp.com/multiplication/primeirovalor/segundovalor <br>' + \
           'https://trab-robson-wallace-d27hec6.herokuapp.com/squareroot/valor <br>' + \
           'https://trab-robson-wallace-d27hec6.herokuapp.com/power/base/expoente <br>' + \
           'https://trab-robson-wallace-d27hec6.herokuapp.com/arithmeticaverage/primeirovalor;segundo;terceiro;... <br>' + \
           'https://trab-robson-wallace-d27hec6.herokuapp.com/harmonicmean/primeirovalor;segundo;terceiro;... <br>' + \
           'https://trab-robson-wallace-d27hec6.herokuapp.com/mod/primeirovalor;segundo;terceiro;... <br>'


# ----------------------------------------------------------------------------------------------------------------------


@app.route('/sum/<value1>/<value2>', methods=['GET'])
def somar(value1, value2):

    try:
        valor1 = int(value1)
    except:
        return 'Primeiro valor inválido.'

    try:
        valor2 = int(value2)
    except:
        return 'Segundo valor inválido.'

    ret = {"Resultado": valor1 + valor2}

    return jsonify(ret)


# ----------------------------------------------------------------------------------------------------------------------


@app.route('/subtraction/<value1>/<value2>', methods=['GET'])
def subtraction(value1, value2):
    try:
        valor1 = int(value1)
    except:
        return 'Primeiro valor inválido.'

    try:
        valor2 = int(value2)
    except:
        return 'Segundo valor inválido.'

    ret = {"Resultado": valor1 - valor2}

    return jsonify(ret)


# ----------------------------------------------------------------------------------------------------------------------


@app.route('/division/<value1>/<value2>', methods=['GET'])
def division(value1, value2):
    try:
        valor1 = int(value1)
    except:
        return 'Primeiro valor inválido.'

    try:
        valor2 = int(value2)
    except:
        return 'Segundo valor inválido.'

    try:
        ret = {"Resultado": valor1 / valor2}
    except ZeroDivisionError:
        return 'Divisão por zero não é possível'

    return jsonify(ret)


# ----------------------------------------------------------------------------------------------------------------------


@app.route('/multiplication/<value1>/<value2>', methods=['GET'])
def multiplication(value1, value2):
    try:
        valor1 = int(value1)
    except:
        return 'Primeiro valor inválido.'

    try:
        valor2 = int(value2)
    except:
        return 'Segundo valor inválido.'

    ret = {"Resultado": valor1 * valor2}

    return jsonify(ret)


# ----------------------------------------------------------------------------------------------------------------------


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
