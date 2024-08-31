import requests
import logging
from bs4 import BeautifulSoup
logger = logging.getLogger(__name__)

LINK_PAGINA = "https://sistemas.ufg.br/CONCURSOS_WEB/"

def extrair_link(elemento): 
    return None

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
        print (concursos_encontrados)
    else:
        logger.info("Nao foi possivel fazer a requisicao ao site do SISCONCURSO.")


if __name__ == '__main__':

    main()