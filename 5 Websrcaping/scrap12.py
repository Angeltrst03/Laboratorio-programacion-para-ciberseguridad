#Jorge Angel Valdez Tristan 1957496
#Importar modulos
import requests
from bs4 import BeautifulSoup as bs

#obtener informacion del url
url = "https://realpython.github.io/fake-jobs/"
page = requests.get(url)

#Analizar html con bs
soup = bs(page.content, "html.parser")
results = soup.find(id="ResultsContainer")

#Buscar elemtos class = card-content
job_elements = results.find_all("div", class_="card-content")
#buscar elementos que contengan la palabra python
python_jobs = results.find_all(
    "h2", string=lambda text:"python" in text.lower()
    )
#buscar elemento de python_elemets y almacenarlos en vriable

python_jobs_elements= [h2_element.parent.parent.parent for h2_element in python_jobs]
#buscar y mostrar inf de los trabajos relac a python
for job_element in python_jobs_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find ("h3", class_="company")
    location_element = job_element.find ("p", class_="location")
    #buscar etiquetas a
    link_url= job_element.find_all("a")[1]["href"]
    print (title_element.text.strip())
    print (company_element.text.strip())
    print(location_element.text.strip())
    #fornatear print para incluir salida del link
    print (f"apply here: {link_url}\n")
    print()
    


    


