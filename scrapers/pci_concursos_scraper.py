import requests
import os
import json
from bs4 import BeautifulSoup

LINK_PAGINA = "https://www.pciconcursos.com.br/concursos/"

def scrape_pciconcursos():
    print("Iniciando requisicao ao site do PCI concursos...")
    response = requests.get(LINK_PAGINA)
    concursos_encontrados = []

    if response.status_code == 200:
        print("Conexao ao site do SISCONCURSO estabelecida com sucesso!!!")
        soup = BeautifulSoup(response.text, 'html.parser')

        div_concursos_fa = soup.find_all("div", {"class": "fa"})
        div_concursos_ea = soup.find_all("div", {"class": "ea"})
        div_concursos_na = soup.find_all("div", {"class": "na"})
        
        for div in div_concursos_fa:
            link = div.find('a').get('href')
            titulo = div.find('a').text.strip()
            descricao = div.find("div", {"class": "cd"}).get_text(separator=" ").strip()
            estado = div.find("div", {"class": "cc"}).get_text(separator=" ").strip()
            data_inscricao = div.find("div", {"class": "ce"}).get_text(separator=" ").strip()
            if estado == '': 
                estado = 'NACIONAL'
            concursos_encontrados.append({
                'titulo':titulo,
                'descricao':descricao,
                'link':link,
                'estado':estado,
                'data_inscricao':data_inscricao
            })
        
        for div in div_concursos_ea:
            link = div.find('a').get('href')
            titulo = div.find('a').text.strip()
            descricao = div.find("div", {"class": "cd"}).get_text(separator=" ").strip()
            estado = div.find("div", {"class": "cc"}).get_text(separator=" ").strip()
            data_inscricao = div.find("div", {"class": "ce"}).get_text(separator=" ").strip()
            if estado == '': 
                estado = 'NACIONAL'
            concursos_encontrados.append({
                'titulo':titulo,
                'descricao':descricao,
                'link':link,
                'estado':estado,
                'data_inscricao':data_inscricao
            })
        
        for div in div_concursos_na:
            link = div.find('a').get('href')
            titulo = div.find('a').text.strip()
            descricao = div.find("div", {"class": "cd"}).get_text(separator=" ").strip()
            estado = div.find("div", {"class": "cc"}).get_text(separator=" ").strip()
            data_inscricao = div.find("div", {"class": "ce"}).get_text(separator=" ").strip()
            if estado == '': 
                estado = 'NACIONAL'
            concursos_encontrados.append({
                'titulo':titulo,
                'descricao':descricao,
                'link':link,
                'estado':estado,
                'data_inscricao':data_inscricao
            })
        
        print(f"{len(concursos_encontrados)} concursos em aberto encontrados...")

        nome_arquivo = f"/tmp/pciconcursos.json"

        with open(nome_arquivo, "w") as f:
            json.dump(concursos_encontrados, f)
