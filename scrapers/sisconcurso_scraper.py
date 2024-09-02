import requests
import re
import json
from bs4 import BeautifulSoup

LINK_PAGINA = "https://sistemas.ufg.br/CONCURSOS_WEB/"

def extrair_link(elemento):
    links_encontrados = []
    for link in elemento.find_all("a"):
        endpoint = link['onclick']
        links_encontrados.append({
                'titulo': link.text, 
                'url': "{0}{1}".format(LINK_PAGINA, re.search(r"'(.*)'", endpoint).group(1))   
            })
    return links_encontrados
    

def scrape_sisconcurso():
    print("Iniciando requisicao ao site do SISCONCURSO...")
    response = requests.get(LINK_PAGINA)
    concursos_encontrados = []

    if response.status_code == 200: 
        print("Conexao ao site do SISCONCURSO estabelecida com sucesso!!!")
        soup = BeautifulSoup(response.text, 'html.parser')
        div_concursos_abertos = soup.find("table", {"class": "listaconcursos"})
        table_concursos = div_concursos_abertos.find("tbody")
        
        for concurso in table_concursos.find_all("tr"):
            concursos_encontrados.append({
                "no_edital" : concurso.find_all("td")[0].text,
                "selecao" : concurso.find_all("td")[1].text,
                "unidade" : concurso.find_all("td")[2].text,
                "concurso-ps" : concurso.find_all("td")[3].text,
                "local" : concurso.find_all("td")[4].text,
                "link" : extrair_link(concurso.find_all("td")[5]),
            })
    else:
        print("Nao foi possivel fazer a requisicao ao site do SISCONCURSO.")

    print(f"{len(concursos_encontrados)} concursos em aberto encontrados...")

    nome_arquivo = f"/tmp/sisconcurso.json"

    with open(nome_arquivo, "w") as f:
     json.dump(concursos_encontrados, f)
