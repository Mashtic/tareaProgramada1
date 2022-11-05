# Creado por: Ian Steven Coto Soto, Fabián Araya
# Fecha de creación: 03/11/2022 0:45 pm
# Última modificación: 03/11/2022 02:10 pm
# Versión: 3.10.8
"""
import requests
import json

API_KEY='jghymCiVrWmRMuT7KImJRYihHID8JcRRGwf2JnLm'

url='https://nasa.api.gov/planetary/apod'

params={
    'api_key': API_KEY,
    'hd': 'True',
    'date': '2010-12-25'
}

response=requests.get(url,params=params)
json_data=json.loads(response.text)
print(json_data)
"""

import nasapy
import os
from datetime import datetime
import urllib.request
from IPython.display import Image,display,Audio
from gtts import gTTS
import pandas
import time
k="jghymCiVrWmRMuT7KImJRYihHID8JcRRGwf2JnLm"

nasa = nasapy.Nasa(key=k)

d= datetime.today().strftime('%Y-%m-%d')

apod = nasa.picture_of_the_day(date=d, hd=True)

print (apod)

def bibliotecaDigital(cedula):
    listatupla=[]
    lista=[]
    ultimo=cedula%10
    for i in range (ultimo):
        d = "algo mistico"
        apod= nasa.picture_of_the_day(date=d, hd=True)
        lista=[apod["title"], apod["date"], apod["explanation"], apod["media_type"], apod["url"]]
        listatupla.append(tuple(lista))
    return listatupla
