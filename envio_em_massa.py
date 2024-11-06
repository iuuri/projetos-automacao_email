import smtplib
import email.utils
from email.message import EmailMessage
from time import sleep

#Configuração de login
EMAIL_ADDRESS = 'iuri.souzasantos1@gmail.com'
EMAIL_PASSWORD = 'jsvz kqpn omby phfg'
contatos = ['iuri.souzasantos@gmail.com', 'iuri.santos@canalrural.com.br']

#Criar e enviar um email 

mail = EmailMessage()
mail['Subject'] = 'Seu pacote chegou com sucesso'
mensagem = """
Olá, esté é um email de validação de automação de email 
"""

mail['From'] = EMAIL_ADDRESS
#fazer um join dos emails
mail['To'] = ', '.join(contatos)
mail.add_header('Content-Type', 'text/html')
mail.set_payload(mensagem.encode('utf-8'))

#Enviar email 
for contato in contatos:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as email:
        email.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        email.send_message(mail)
        #pausas para evitar bloqueios no provedor
        sleep(60)