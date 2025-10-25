import requests
from bs4 import BeautifulSoup

url = "https://buscador.masterendaw.es/"

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")

valor = soup.find(id= "totalCompanies").text
print(f"{valor}")