from bs4 import BeautifulSoup
import requests
from model import session

sitio ='http://www.lohechoenmexico.mx/mximg6/'
pagina ='mximg_galeria.php' 
r = requests.get(sitio+pagina)

sopa = BeautifulSoup(r.text, 'html.parser')
articulos = sopa.find_all('article')

for articulo in articulos:
    estado = articulo.find('p', 'post-date')
