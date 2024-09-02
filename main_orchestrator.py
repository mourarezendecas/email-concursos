from scrapers.sisconcurso_scraper import scrape_sisconcurso
from database.database_connection import get_emails
from email_package.email_sender import send_email


def execute_scrapers():
    print("Iniciando execução de scrapers...")
    print("Acionando scrape do SISCONCURSO...")
    scrape_sisconcurso()
    print("Processo de scraping completo!!!")


def send_emails():
    print("Iniciando requisição ao banco de dados para obter a lista de emails...")
    emails_list = get_emails()
    print(f"{len(emails_list)} emails obtidos, iniciando processo de envio!!!")
    for email in emails_list:
        send_email(email)


if __name__ == '__main__':
    execute_scrapers()
    send_emails()