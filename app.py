from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/add/<int:num1>/<int:num2>')
def add_numbers(num1, num2):
    result = str(num1 + num2)
    return render_template('result.html', result=result)

@app.route('/multiply/<int:num1>/<int:num2>')
def multiply_numbers(num1, num2):
    result = str(num1 * num2)
    return render_template('result.html', result=result)

@app.route('/subtract/<int:num1>/<int:num2>')
def subtract_numbers(num1, num2):
    result = str(num1 - num2)
    return render_template('result.html', result=result)

@app.route('/divide/<int:num1>/<int:num2>')
def divide_numbers(num1, num2):
    try:
        result = str(num1 / num2)
        return render_template('result.html', result=result)
    except ZeroDivisionError:
        result = "Cannot divide by zero!"
        return render_template('result.html', result=result)
          

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)