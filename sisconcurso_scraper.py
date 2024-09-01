import requests
import logging
import re
from bs4 import BeautifulSoup
logger = logging.getLogger(__name__)

LINK_PAGINA = "https://sistemas.ufg.br/CONCURSOS_WEB/"

def extrair_link(elemento):
    links_encontrados = []
    for link in elemento.find_all("a"):
        endpoint = link['onclick']
        print(endpoint)
        links_encontrados.append({
                'titulo': link.text, 
                'url': f"{LINK_PAGINA}{re.search(r"\'(.*)\'\)", endpoint).group(1)}"
            })
    return links_encontrados
    

def main():
    logging.basicConfig(filename='email-concursos.log', level=logging.INFO)

    logger.info("Iniciando requisicao ao site do SISCONCURSO...")
    response = requests.get(LINK_PAGINA)

    if response.status_code == 200: 
        logger.info("Conexao ao site do SISCONCURSO estabelecida com sucesso!!!")
        logger.info(response)
        soup = BeautifulSoup(response.text, 'html.parser')
        div_concursos_abertos = soup.find("table", {"class": "listaconcursos"})
        table_concursos = div_concursos_abertos.find("tbody")
        concursos_encontrados = []
        for concurso in table_concursos.find_all("tr"):
            concursos_encontrados.append({
                "no_edital" : concurso.find_all("td")[0].text,
                "selecao" : concurso.find_all("td")[1].text,
                "unidade" : concurso.find_all("td")[2].text,
                "concurso/ps" : concurso.find_all("td")[3].text,
                "local" : concurso.find_all("td")[4].text,
                "link" : extrair_link(concurso.find_all("td")[5]),
            })
    else:
        logger.info("Nao foi possivel fazer a requisicao ao site do SISCONCURSO.")

    logger.info(f"{len(concursos_encontrados)} concursos em aberto encontrados...")

if __name__ == '__main__':

    main()