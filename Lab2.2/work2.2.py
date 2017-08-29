from flask import *
import sys
import re
import glob
import pprint

app = Flask(__name__)

@app.route('/')
@app.route('/index')

def index():
    return "Любой рандомный текст"

@app.route('/python')
def python():
    return jsonify(str(sys.__dict__))


@app.route('/configs')
def config():
    r=[]
    for h in val.keys():
        r.append(val[h]['name'])
    return jsonify(r)

@app.route('/configs/<hostname>')
def host(hostname):
    for h in val.keys():
        if val[h]['name']==hostname:
            return jsonify(val[h]['addresses'])
    return jsonify('Not Found')


if __name__ == '__main__':
    val = {}
    for rlist in glob.glob(('C:\\Users\\A.Meshkov\\Seafile\\p4ne_training\\config_files\\*.txt')):
        val[rlist] = {}
        val[rlist]['addresses'] = []
        with open(rlist) as f:
            for x in f:
                a = re.match("^hostname (.+)", x)
                if a:
                    val[rlist]['name'] = a.group(1)
                    continue
                a = re.match("^ ip address ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+) ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)",
                                x)
                if a:
                    val[rlist]['addresses'].append({'ip': a.group(1), 'mask': a.group(2)})

app.run(debug=True)