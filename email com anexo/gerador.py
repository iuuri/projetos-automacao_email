arquivos = ['csv_exemplo.csv', 'exemplo_word.docx',
            'ExemploPlanilha.xlsx', 'PDF_Exemplo.pdf', 'Untitled presentation.pptx','img.jpg']

for item in arquivos:
    with open(item,'w') as f:
        f.write(item)