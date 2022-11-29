#Jorge Angel Valdez Tristan 1957496
# modulos a importar
import requests
import csv
from bs4 import BeautifulSoup
# direccion de la pagina
url = "http://quotes.toscrape.com/"
#get requests
response= requests.get(url)
#aNALIZAR EL BS4
html = BeautifulSoup(response.text, "html.parser")
#Extraer citas y autores
quotes_html = html.find_all("span", class_="text")
authors_html = html.find_all("small", class_="author")
#crear lista de citas
quotes = list()
for quote in quotes_html:
    quotes.append(quote.text)
#crear lista de autores
authors = list()
for author in  authors_html:
    authors.append(author.text)
#combinar citas y autores
for t in zip (quotes, authors):
    print (t)
#guardar citas y autores en un csv en el directorio actual
# Abrir el archivo con excel / libreoffice, etc
with open ("./matriculas.csv", "w") as csv_file:
    csv_writer = csv.writer(csv_file, dialect = "excel")
    csv_writer.writerows(zip(quotes, authors))
    
    
    
