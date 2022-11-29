 #Autor: Jorge Angel Valdez Tristan 
# Matrícula: 1957496
import requests

def get_pokemons(url = 'https://pokeapi.co/api/v2/pokemon-form', offset = 0):
    args = {'offset' : offset} if offset else {}
    respuesta = requests.get(url, params=args)
    if respuesta.status_code == 200:
        resultados = respuesta.json().get('results', [])
        if resultados:
            for pokemon in resultados:
                print(pokemon['name'])
            next = input('¿Continuar listando? [y/n] ').lower()
            if next == 'y':
                get_pokemons(offset=offset+20)

if __name__ == '__main__':
    get_pokemons()
