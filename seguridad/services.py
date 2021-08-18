import requests
import json

def generate_request_post(url, params={}):
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(params),headers=headers)
    if response.status_code == 200:
        return response.json()

def generate_request_get(url, params={}):
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()


#CONFIGURACION
def get_componentes(params={}):
    response = generate_request_get('http://127.0.0.1:8000/api-seguridad/componentes/', params)
    if response:
       user = response.get('componentes')
       return user

    return ""
def estadoComponente(params={}):
    print(params)
    response = generate_request_post('http://127.0.0.1:8000/api-seguridad/componentes/', params)
    if response:
        user = response.get('mensaje')
        return user
    return ""


def get_historial(params={}):
    response = generate_request_get('http://127.0.0.1:8000/api-seguridad/historial/', params)
    if response:
       user = response.get('historial')
       return user
    return ""