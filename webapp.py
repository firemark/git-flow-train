from flask import Flask
from flask import render_template
from fetch_data import to_list
from collections import namedtuple
from itertools import starmap
app = Flask(__name__)
data = namedtuple("Data", "country local_price dollar_ex dollar_price dollar_ppp dollar_valuation")

def load_data():
    return to_list('data.csv')

@app.route('/')
def hello_world():
    headers, *body = load_data()
    body = starmap(data, body)
    return render_template('index.html', data=body, headers=headers)
