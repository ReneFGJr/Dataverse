import requests
import os

# Definir variáveis (substitua pelos valores reais)
PARENT = 'teste'

# URL da API do Dataverse (substitua pelo seu)
SERVER_URL = 'https://cedapdados.ufrgs.br/api'

# Chave de API do Dataverse (substitua pela sua)
API_TOKEN = "6a680d93-23ab-4471-ab8e-26e880d2ee14"

# Caminho para o arquivo JSON
json_file = './dataset.json'

# Cabeçalhos da solicitação
headers = {
    "X-Dataverse-key": API_TOKEN,
    "Content-Type": "application/json"
}

# URL da API para criar o dataset
url = f"{SERVER_URL}/api/dataverses/{PARENT}/datasets"

# Abrir e ler o conteúdo do arquivo JSON
with open(json_file, 'r', encoding='utf-8') as f:
    dataset_metadata = f.read()

# Fazer a requisição POST para enviar o arquivo JSON
response = requests.post(url, headers=headers, data=dataset_metadata)

# Verificar o resultado
if response.status_code == 201:
    print("Dataset criado com sucesso!")
    print("Resposta da API:", response.json())
else:
    print("Erro ao criar dataset:", response.status_code)
    print("Detalhes do erro:", response.text)
