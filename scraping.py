import requests # Permite conectar con la pagina web y obtener el codigo html en texto
from bs4 import BeautifulSoup # Analiza y lee el HTML de la página
from bs4.element import Tag # Representa un elemnto HTML en especifico 
from typing import cast # Indica al programa que trate a un elemento como un tipo en especifico


try:
    url = "https://buscador.masterendaw.es/"
    conexion_url = requests.get(url).text # Conectamos y obtenemos el codigo de la pagina web

    analizamos_web = BeautifulSoup(conexion_url, "html.parser") # Analizamos el HTML para poder trabajar con él 
    if analizamos_web is None:
        print("Error al parsear el HTML")
        exit(1)

    elemento_encontrar = cast(Tag, analizamos_web.find(id= "totalCompanies")) # Buscamos el elemento con ese ID
    if elemento_encontrar is None:
        print("Error al encontrar el elemento")
        exit(1)
    
    print(f"{elemento_encontrar.get_text(strip=True)}") # Imprime solo el texto del elemento (sin las etquestas ni espacios)

except requests.exceptions.InvalidURL as e:
    print("URL invalida:", e)
except requests.exceptions.ConnectionError as e:
    print("Error de conexión:", e)
except requests.exceptions.RequestException as e:
    print("Error al hacer la solicitud:", e)