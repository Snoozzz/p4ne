from flask import Flask
import sys
import re

app = Flask(__name__)

@app.route('/')
@app.route('/index')

def index():
    return "Любой рандомный текст"

@app.route('/python')
def python():
    return sys.__dict__


@app.route('/configs')
def class_ip(x):
    a = re.match("^hostname (.+)", x)
    if a:
        return ("HOST", a.group(1))
#@app.route('/config/hostname')

if __name__ == '__main__':
    app.run(debug=True)