from scrapers.sisconcurso_scraper import scrape_sisconcurso
from scrapers.pci_concursos_scraper import scrape_pciconcursos
from database.database_connection import get_users
from email_package.email_sender import send_email


def execute_scrapers():
    print("Iniciando execução de scrapers...")
    print("Acionando scrape do SISCONCURSOS...")
    scrape_sisconcurso()
    print("Acionando scrape do PCI CONCURSOS...")
    scrape_pciconcursos()
    print("Processo de scraping completo!!!")


def send_emails():
    print("Iniciando requisição ao banco de dados para obter a lista de emails...")
    users = get_users()
    print("Iniciando processo de envio!!!")
    for user in users:
        send_email(user)

def execute():
    execute_scrapers()
    send_emails()