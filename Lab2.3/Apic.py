import requests, json, pprint

def new_ticket():
    url = 'https://sandboxapic.cisco.com/api/v1/ticket'
    payload = {"username": "devnetuser",
               "password": "Cisco123!"
              }
    header = {"content-type": "application/json"}

    response = requests.post(url, data=json.dumps(payload),
                             headers=header, verify=False)

    return response.json()['response']['serviceTicket']

if __name__ == '__main__:':

    ticket = new_ticket()
    controller = "devnetapi.cisco.com/sandbox/apic_em"
    url = "https://" + controller + "/api/v1/host?limit=1&offset=1"
    header = {"content-type": "application/json",
              "X-Auth-Token":ticket
             }

    responce = requests.get(url, headers=header, verify=False)

    print("Hosts = ")
    #pprint.pprint(json.dumps(responce.json()))
