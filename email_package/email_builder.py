import os
import json
from datetime import datetime
DATA_ATUAL = datetime.today().strftime('%d %m %Y')


CURRENT_DIR = os.path.dirname(__file__)
PROJECT_DIR = os.path.abspath(os.path.join(CURRENT_DIR, '..'))
SISCONCURSO_PATH = os.path.join(PROJECT_DIR, 'json-concursos')

def retorna_email(nome_usuario):
    return f"""
<!DOCTYPE html>
<style>
    f{retorna_style()}
</style>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Concursos pelo Brasil</title>
</head>
<body>
    <table width="100%" cellpadding="0" cellspacing="0" border="0">
        <tr>
            <td align="center">
                <table width="600" cellpadding="0" cellspacing="0" border="0">
                    <body style="font-family: 'Poppins', Arial, sans-serif">
                        <table width="100%" border="0" cellspacing="0" cellpadding="0">
                            <tr>
                                <td align="center" style="padding: 20px;">
                                    <table class="content" width="600" border="0" cellspacing="0" cellpadding="0" style="border-collapse: collapse; border: 1px solid #cccccc;">
                                        <!-- Header -->
                                        <tr>
                                            <td class="header" style="background-color: #345C72; padding: 40px; text-align: center; color: white; font-size: 24px;">
                                            Concursos pelo Brasil - Newsletter
                                            </td>
                                        </tr>
                    
                                        <!-- Body -->
                                        <tr>
                                            <td class="body" style="padding: 40px; text-align: left; font-size: 16px; line-height: 1.6;">
                                            Olá, {nome_usuario}! <br>
                                            Abaixo, segue em anexo os concursos com inscrições abertas encontrados.
                                            <br>
                                            {retorna_elemento_sisconcurso()}
                                            </td>
                                        </tr>
                                        <tr>
                                            <td class="footer" style="background-color: #333333; padding: 40px; text-align: center; color: white; font-size: 14px;">
                                            {DATA_ATUAL} | Concursos pelo Brasil
                                            <br>
                                            Caso não deseja receber mais estes e-mails, por favor contactar gabrielcastrorezende@gmail.com
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                        </table>
                    </body>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
"""

def retorna_elemento_sisconcurso():
    with open(f'{SISCONCURSO_PATH}/sisconcurso.json') as file:
        data = json.load(file)
    
    elementos = []
    
    if len(data)>0:
        for i in data:
            elementos.append(f"""<li><a href="{i['link'][0]['url']}"> {i['selecao']} | {i['unidade']} | {i['concurso-ps']} | {i['local']}</a></li>""")
        lista = f"""<ul><strong>SISCONCURSOS</strong>{'<br>'.join(elementos)}</ul>"""
        return lista
    else:
        lista = f"""<ul><strong>SISCONCURSOS</strong><br>Nenhum concurso disponibilizado no sisconcursos.</ul>"""

    
def retorna_style():
    return """
    @media screen and (max-width: 600px) {
      .content {
          width: 100% !important;
          display: block !important;
          padding: 10px !important;
      }
      .header, .body, .footer {
          padding: 20px !important;
      }
    }
"""