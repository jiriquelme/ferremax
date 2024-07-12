import requests
import json

# Create your views here.

dolar = requests.get('https://si3.bcentral.cl/SieteRestWS/SieteRestWS.ashx?user=jos3.riquelme@outlook.com&pass=Benji1998.&firstdate=2024-05-27&timeseries=F073.TCO.PRE.Z.D&function=GetSeries').text

dolar_response = json.loads(dolar)

valorDolar = dolar_response["Series"]["Obs"][0]["value"]



print(valorDolar)
    
