from flask import Flask
from flask import render_template
from to_dict import to_dict
app = Flask(__name__)


def load_data():
    return to_dict('data.csv')

@app.route('/')
def hello_world():
    data = load_data()
    headers = data[0]
    print(headers)
    body = data[1:]
    print list(body)
    # print(body)
    
    return render_template('index.html', data=data, headers=headers)
