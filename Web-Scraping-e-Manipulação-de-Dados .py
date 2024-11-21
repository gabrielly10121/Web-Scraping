
import requests
from bs4 import BeautifulSoup, Comment
import json
import csv
from openpyxl import Workbook


url = 'https://www.imepac.edu.br'

try:
   
    response = requests.get(url, timeout=5)  
    response.raise_for_status()  
   
    soup = BeautifulSoup(response.content, 'html.parser')
except requests.exceptions.RequestException as e:
    
    print(f"Erro ao acessar o site: {e}")
    soup = None  

if soup:
    print("\n** Extração de dados do site **\n")

    
    titulos = [t.get_text(strip=True) for t in soup.find_all(['h1', 'h2', 'h3'])]
    print("Títulos encontrados:", titulos)

    imagens = [img['src'] for img in soup.find_all('img') if 'src' in img.attrs]
    print("Imagens encontradas:", imagens)

    tabelas = [str(tab) for tab in soup.find_all('table')]
    print("Tabelas encontradas:", tabelas)

    cabecalhos = [cab.get_text(strip=True) for cab in soup.find_all(['header', 'nav'])]
    print("Cabeçalhos encontrados:", cabecalhos)

    print("\n** Exportando os dados **\n")

    
    dados = {'titulos': titulos, 'imagens': imagens, 'tabelas': tabelas, 'cabecalhos': cabecalhos}
    with open('dados.json', 'w', encoding='utf-8') as json_file:
        json.dump(dados, json_file, ensure_ascii=False, indent=4)
    print("Dados exportados para 'dados.json'.")

   
    with open('dados.csv', 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Tipo', 'Conteúdo']) 
        writer.writerows([('Título', titulo) for titulo in titulos])
        writer.writerows([('Imagem', img) for img in imagens])
        writer.writerows([('Tabela', tabela) for tabela in tabelas])
        writer.writerows([('Cabeçalho', cab) for cab in cabecalhos])
    print("Dados exportados para 'dados.csv'.")

    
    try:
        workbook = Workbook()
        sheet = workbook.active
        sheet.title = 'Dados Extraídos'  
        sheet.append(['Tipo', 'Conteúdo'])  

       
        for titulo in titulos:
            sheet.append(['Título', titulo])
        for img in imagens:
            sheet.append(['Imagem', img])
        for tabela in tabelas:
            sheet.append(['Tabela', tabela])
        for cab in cabecalhos:
            sheet.append(['Cabeçalho', cab])

        
        excel_filename = 'dados.xlsx'
        workbook.save(excel_filename)  
        print(f"Arquivo Excel criado com sucesso: {excel_filename}")

    except Exception as e:
        print(f"Erro ao criar o arquivo Excel: {e}")

    print("\n** Manipulação do HTML **\n")

    
    novo_p = soup.new_tag('p')
    novo_p.string = 'Novo parágrafo adicionado.'
    soup.body.append(novo_p)
    print("Nova tag <p> adicionada ao HTML.")

    
    tag_p = soup.find('p')
    if tag_p:
        tag_p.string = 'Fomos expostos!'
        print("Texto da primeira tag <p> alterado para: 'Fomos expostos!'")

    
    print("\nHTML Modificado:")
    print(soup.prettify())

    print("\n** Análise de componentes do HTML **\n")

    
    print("Tags encontradas:")
    for tag in soup.find_all(True):  
        print(f"- {tag.name}")

    
    print("\nStrings encontradas:")
    for string in soup.stripped_strings:  
        print(f"- {string}")

   
    print("\nComentários encontrados:")
    for comment in soup.find_all(string=lambda text: isinstance(text, Comment)):  
        print(f"- {comment}")

else:
    print("Não foi possível continuar com o scraping devido a problemas na conexão com o site.")
