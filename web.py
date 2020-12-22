from flask import Flask

from calculator import sum, subtract, multiply, divide


app = Flask(__name__)

@app.route('/')
def index():
    return """
    <h1>Olist Calculator</h1>
    <ol>
        <li><a href='/sum'>Sum</a>
        <li><a href='/subtract'>Subtract</a>
        <li><a href='/multiply'>Multiply</a>
        <li><a href='/divide'>Divide</a>
    </ol>
    """

@app.route('/sum')
def sum_numbers():
    n1 = 1.0
    n2 = 2.0
    result = sum(n1, n2)
    return f"""
    <h1>Olist Calculator</h1>
    <h3>The sum {n1} + {n2} is: {result}</h3>
    <a href='/'>Go Back</a> 
    """

@app.route('/subtract')
def subtract_numbers():
    n1 = 1.0
    n2 = 2.0
    result = subtract(n1, n2)
    return f"""
    <h1>Olist Calculator</h1>
    <h3>The subtraction {n1} - {n2} is: {result}</h3>
    <a href='/'>Go Back</a> 
    """

@app.route('/multiply')
def multiply_numbers():
    n1 = 1.0
    n2 = 2.0
    result = multiply(n1, n2)
    return f"""
    <h1>Olist Calculator</h1>
    <h3>The multiplication {n1} * {n2} is: {result}</h3>
    <a href='/'>Go Back</a> 
    """

@app.route('/divide')
def divide_numbers():
    n1 = 1.0
    n2 = 2.0
    result = divide(n1, n2)
    return f"""
    <h1>Olist Calculator</h1>
    <h3>The division {n1} / {n2} is: {result}</h3>
    <a href='/'>Go Back</a> 
    """

app.run(debug=True)