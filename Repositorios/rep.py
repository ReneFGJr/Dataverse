import requests
from bs4 import BeautifulSoup
import csv

# URL da página que contém os repositórios
url = "http://rbrd.ibict.br/como-fazer-parte-da-rede/"

# Enviar uma requisição para o site
response = requests.get(url)

# Verificar se a requisição foi bem-sucedida
if response.status_code == 200:
    # Parsear o conteúdo HTML
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encontrar todos os links de repositórios na página
    repositórios = []  # Lista para armazenar os repositórios extraídos

    # Exemplo de estrutura de onde os dados estariam
    for link in soup.find_all('a', href=True):
        if "repositorio" in link['href']:  # Apenas pegar links relacionados a repositórios
            nome = link.get_text().strip()  # Nome do repositório
            nome = nome.replace(chr(13),'')
            nome = nome.replace(chr(10),'')
            while '  ' in nome:
                nome = nome.replace('  ',' ')

            url_repositorio = link['href']  # URL do repositório
            url_repositorio = url_repositorio.strip()
            # Aqui, podemos ajustar manualmente a região ou implementar lógica para buscar
            região = "Região não definida"

            repositórios.append(['"'+url_repositorio+'"','"'+ nome +'"', '"'+região+'"'])

    # Salvar os repositórios em um arquivo CSV
    with open('repositorios_rbrd.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Link", "Nome do Repositório", "Região"])
        writer.writerows(repositórios)

    print("Arquivo CSV gerado com sucesso!")
else:
    print(f"Falha ao acessar a página. Status code: {response.status_code}")
