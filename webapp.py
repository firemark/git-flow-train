from flask import Flask
from flask import render_template
app = Flask(__name__)


def load_data():
    return [{'country': 'Ala', 'local_price': 21, 'dollar_ex':2, 'dollar_price': 11, 'dollar_ppp': 4, 'dollar_valuation': 22},
            {'country': 'AlASa', 'local_price': 21, 'dollar_ex':2, 'dollar_price': 11, 'dollar_ppp': 4, 'dollar_valuation': 22}]
@app.route('/')
def hello_world():
    data = load_data()
    headers = data[0]
    print(headers)
    body = data[1:]
    print list(body)
    # print(body)
    
    return render_template('index.html', data=data, headers=headers)
