import requests
import pprint

r = requests.get('https://lookup.binlist.net/40587031', headers={'Accept-Version':'3'})

pprint.pprint(r.json())
