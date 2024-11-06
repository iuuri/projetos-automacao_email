from email_sender import Emailer

#Email e senha do remetente 
email = Emailer('iuri.souzasantos1@gmail.com', 'jsvz kqpn omby phfg')

#Contatos para receber os emails
lista_contatos = ['iuri.souzasantos@gmail.com',
                  'iuri.santos@canalrural.com.br']


#Corpo do email
mensagem = '''
Olá seu pacote acaba de chegar nos correios!
'''

#Configuração do email
email.definir_conteudo(topico='Seu pacote chegou!', email_remetente='iuri.souzasantos1@gmail.com',
                       lista_contatos=lista_contatos, conteudo_email=mensagem)

#caso precise anexar imagens ou outros tipos de arquivos
imagens = ['teste.png']
email.anexar_imagem(imagens)

arquivos = ['csv_exemplo.csv', 'exemplo_word.docx',
            'ExemploPlanilha.xlsx', 'PDF_Exemplo.pdf', 'Untitled presentation.pptx']

#função para anexar os arquivos
email.anexar_arquivos(arquivos)

#função para configurar intervalo de tempo e enviar email 
email.enviar_email(intervalo_em_segundos=30)