from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add/<int:a>/<int:b>')
def add_numbers(a, b):
        return str(a + b)

@app.route('/mult/<int:a>/<int:b>')
def multiply_numbers(a, b):
        return str(a * b)

@app.route('/subtr/<int:a>/<int:b>')
def subtract_numbers(a, b):
        return str(a - b)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)