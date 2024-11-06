import smtplib
import email.utils
from email.message import EmailMessage
import imghdr

#Configuração de login
EMAIL_ADDRESS = 'iuri.souzasantos1@gmail.com'
EMAIL_PASSWORD = 'jsvz kqpn omby phfg'

#Criar e enviar um email 

mail = EmailMessage()
mail['Subject'] = 'Seu pacote chegou com sucesso'
mensagem = """
Olá, esté é um email de validação de automação de email 
"""

mail['From'] = EMAIL_ADDRESS
mail['To'] = 'iuri.souzasantos@gmail.com'
mail.add_header('Content-Type', 'text/html')
mail.set_payload(mensagem.encode('utf-8'))

#Anexar arquivos 
imagens =['teste.png']
for imagem in imagens:
    with open(imagem, 'rb') as arquivo:
        dados = arquivo.read()
        extensao_imagem = imghdr.what(arquivo.name)
        nome_arquivo = arquivo.name
        mail.add_attachment(dados, maintype='image', subtype=extensao_imagem, filename=nome_arquivo)

#Anexar arquivos de qualquer tipo de extensão(que não seja imagem)
arquivos = ['csv_exemplo.csv', 'exemplo_word.docx',
            'ExemploPlanilha.xlsx', 'PDF_Exemplo.pdf', 'Untitled presentation.pptx']

for arquivo in arquivos:
    with open(arquivo, 'rb') as arquivo:
        dados = arquivo.read()
        nome_arquivo = arquivo.name
        mail.add_attachment(dados, maintype='application', subtype='octet-stream', filename=nome_arquivo)


#Enviar email 
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as email:
    email.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    email.send_message(mail)