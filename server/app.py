#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return'<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print (f'{parameter}')
    return f'{parameter}'
    

@app.route('/count/<int:parameter>')
def count(parameter):
    number = ''
    for num in range(parameter):
        number += f'{num}\n'
    return number

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        return f'{num1+num2}'
    elif operation == '-':
        return f'{num1-num2}'
    elif operation == 'div':
        return f'{num1 / num2}'
    elif operation == '*':
        return f'{num1 * num2}'
    elif operation == '%':
        return f'{num1 % num2}'
    else:
        print ("Invalid entry")
    

  

if __name__ == '__main__':
    app.run(port=5555, debug=True)
