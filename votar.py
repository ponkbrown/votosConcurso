import requests
headers = {'User-Agent': 'Mozilla/5.0'}
payload = {'ID':'14720'}
session = requests.Session()
session.post('http://www.lohechoenmexico.mx/mximg6/voto.php', headers=headers, data=payload)
