from flask import Flask
from flask import render_template
from collections import namedtuple

app = Flask(__name__)

data = namedtuple('Row', 'country local_price dollar_ex dollar_price dollar_ppp dollar_valuation')

def load_data():
    return [data('Ala', 32, 21, 312, 32, 23), 
            data('Ahoy', 214, 2, 13, 2, 1)]

@app.route('/')
def hello_world():
    return render_template('index.html', data=load_data())


@app.route('/hello/<name>')
def hello(name=None):
    return render_template('index.html', name=name)

