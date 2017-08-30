import requests, json, pprint
from flask import *
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("topology.html")

@app.route('/hosts')
def hosts1():
    return jsonify(hosts())

@app.route('/ndevices')
def NDevices1():
    return jsonify(NDevices())

@app.route('/api/topology')
def topology1():
    return jsonify(Topology())


def new_ticket():
    url = 'https://sandboxapic.cisco.com/api/v1/ticket'
    payload = {"username": "devnetuser",
               "password": "Cisco123!"
              }
    header = {"content-type": "application/json"}

    response = requests.post(url, data=json.dumps(payload),
                             headers=header, verify=False)

    return response.json()['response']['serviceTicket']

def hosts():
    ticket = new_ticket()
    controller = "devnetapi.cisco.com/sandbox/apic_em"
    url = "https://" + controller + "/api/v1/host"
    header = {"content-type": "application/json",
              "X-Auth-Token": ticket
              }
    response = requests.get(url, headers=header, verify=False)
    print("Hosts = ")
    pprint.pprint(json.dumps(response.json()))
    return response.json()['response']

def NDevices():
    ticket = new_ticket()
    controller = "devnetapi.cisco.com/sandbox/apic_em"
    url = "https://" + controller + "/api/v1/network-device"
    header = {"content-type": "application/json",
              "X-Auth-Token": ticket
              }
    response = requests.get(url, headers=header, verify=False)
    print("NDevices = ")
    pprint.pprint(json.dumps(response.json()))
    return response.json()['response']

def Topology():
    ticket = new_ticket()
    controller = "devnetapi.cisco.com/sandbox/apic_em"
    url = "https://" + controller + "/api/v1/topology/physical-topology"
    header = {"content-type": "application/json",
              "X-Auth-Token": ticket
              }
    response = requests.get(url, headers=header, verify=False)
    print("Topology = ")
    pprint.pprint(json.dumps(response.json()))
    return response.json()['response']

#if __name__ == '__main__:':


app.run(debug=True)