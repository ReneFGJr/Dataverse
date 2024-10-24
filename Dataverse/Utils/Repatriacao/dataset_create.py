import requests
import json

# URL da API do Dataverse (substitua pelo seu)
dataverse_url = 'https://cedapdados.ufrgs.br/api'

# Identificador do Dataverse onde o dataset será criado
dataverse_identifier = "teste"

# Chave de API do Dataverse (substitua pela sua)
api_key = "6a680d93-23ab-4471-ab8e-26e880d2ee14"

# Carregar o JSON com os dados do dataset
json_file = "./dataset.json"

# Ler o conteúdo do arquivo JSON
with open(json_file, 'r', encoding='utf-8') as f:
    dataset_metadata = json.load(f)

# Endpoint da API para criar o dataset
url = f"{dataverse_url}/api/dataverses/{dataverse_identifier}/datasets"
#url = f"{dataverse_url}/api/v1/dataverses/{dataverse_identifier}/datasets"

# Cabeçalhos da solicitação, incluindo a API key para autenticação
headers = {
    "X-Dataverse-key": api_key,
    "Content-Type": "application/json"
}

# Fazer a requisição POST para criar o dataset
response = requests.post(url, headers=headers, json=dataset_metadata)

# Verificar o resultado
if response.status_code == 201:
    print("Dataset criado com sucesso!")
    print("Resposta da API:", response.json())
else:
    print("Erro ao criar dataset:", response.status_code)
    print("Detalhes do erro:", response.text)
