import requests
import json
#Jorge Angel Vladez Tristan
#1957496
if __name__=="__main__":
  url="http://httpbin.org/post"
  argumentos={"nombre":"Jorge","Matricula":"1957496","curso":"Laboratorio de programacion para ciberseguridad"}

  response = requests.post(url, params=argumentos)
  if response.status_code ==200:
    print(response.content)
  