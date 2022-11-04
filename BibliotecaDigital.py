# Creado por: Ian Steven Coto Soto, Fabián Araya
# Fecha de creación: 03/11/2022 0:45 pm
# Última modificación: 03/11/2022 02:10 pm
# Versión: 3.10.8
import requests
import json
API_KEY='jghymCiVrWmRMuT7KImJRYihHID8JcRRGwf2JnLm'

url='https://apod.nasa.gov/apod'

params={
    'api_key': API_KEY, 
    'hd': "True",
    'date':"2020-12-25"
    
}

response=requests.get(url, params=params)
json_data=json.loads(response.text)
print(json_data)