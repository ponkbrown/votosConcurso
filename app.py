from bs4 import BeautifulSoup
import requests
from model import session, Foto
import time


sitio ='http://www.lohechoenmexico.mx/mximg6/'
galeria ='mximg_galeria.php?'
pagina = 'pageNum_gal='
numero = 0
for numero in range(1222,1251):
    print( '\n\n')
    print('PAGINA: '+ str(numero))
    print( '\n\n')

    try:
        r = requests.get(sitio+galeria+pagina+str(numero))
        print(r.status_code)
    except:
        time.sleep(60)
        continue

    sopa = BeautifulSoup(r.text, 'html.parser')
    articulos = sopa.find_all('article')

    for articulo in articulos:
        estado = articulo.find('p', 'post-date').text
        autor = articulo.h2.strong.text
        link = articulo.find('div', 'entry excerpt').p.a.get('href')
        url = (sitio+link)
        try:
            votaPage = requests.get(url)
        except:
            time.sleep(60)
            continue
        vSopa = BeautifulSoup(votaPage.text,'html.parser')
        postRows = vSopa.find_all('div', 'post-row')
        for postRow in postRows:
            if postRow.img:
                votos = int(postRow.find('span').text)
                # un minihack por que no esta bien estructurado el html de la pagina
                brs = postRow.find_all('br')
                br = brs[0]
                titulo = br.text.split('\n\n')[0].strip()

        print('Titulo: {0}\nAutor: {1}\nEstado: {2}\nVotos: {3}\nUrl: {4}'.format(titulo,autor,estado,votos,url))
        print('====='*15)
        fotodb = Foto(Autor=autor, Estado=estado,Titulo=titulo,Url=url,votos=votos)
        session.add(fotodb)
        # Este sleep es para no saturar al servidor
        time.sleep(.3)
    session.commit()
