import requests

def generate_request(url, params={}):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()

def get_componentes(params={}):
    response = generate_request('http://127.0.0.1:8000/api-seguridad/componentes/', params)
    if response:
       user = response.get('componentes')
       return user

    return ""