import requests
import json
import os

# Configurações
API_URL = "https://vitrinedadosabertos-dev.rnp.br/api"
#API_URL = "https://hdatarepository.ipen.br/api"
API_KEY = "f29f846b-49fe-4d67-a56f-0bd36bdd05a8"
#API_KEY = "89a5c2b0-880a-4b46-b4e1-3221d95113b0"
DATAVERSE_ALIAS = "repatriacao"
FILE_JSON = 'metadata.json'

# Verificar se o arquivo JSON existe
if not os.path.exists(FILE_JSON):
    print(f"Erro: O arquivo {FILE_JSON} não foi encontrado.")
    exit(1)

# Carregar metadados do arquivo local
with open(FILE_JSON, "r", encoding="utf-8") as file:
    metadata = json.load(file)

# Função para corrigir campos com "multiple: false" ou compostos
def fix_metadata_fields(fields):
    for field in fields:
        if "multiple" in field and field["multiple"] is False and isinstance(field.get("value"), list):
            field["value"] = field["value"][0] if len(field["value"]) > 0 else ""
        if field.get("typeClass") == "compound" and "value" in field:
            fix_metadata_fields(field["value"])

# Preparar os metadados
metadata_blocks = metadata["latestVersion"]["metadataBlocks"]
fix_metadata_fields(metadata_blocks["citation"]["fields"])

# Alterar o título do dataset
for field in metadata_blocks["citation"]["fields"]:
    if field["typeName"] == "title" and isinstance(field["value"], str):
        field["value"] = f"Dados repatriados: {field['value']}"

# Configurar o DOI explicitamente
dataset_metadata = {
    "datasetVersion": {
        "metadataBlocks": metadata_blocks
    },
    "identifier": metadata["identifier"],  # DOI original
    "protocol": metadata["protocol"],      # Protocolo usado (DOI)
    "authority": metadata["authority"],    # Autoridade do DOI
    "storageIdentifier": metadata["storageIdentifier"]
}

# Endpoint para criação do dataset
endpoint = f"{API_URL}/dataverses/{DATAVERSE_ALIAS}/datasets/:import?pid={metadata['persistentUrl']}"

# Configuração do cabeçalho
headers = {
    "X-Dataverse-key": API_KEY,
    "Content-Type": "application/json"
}

# Logs para depuração
print("Enviando os seguintes metadados para a API:")
print(json.dumps(dataset_metadata, indent=4, ensure_ascii=False))

# Enviar solicitação para criar o dataset
response = requests.post(endpoint, headers=headers, json=dataset_metadata, verify=False)

# Verificar resposta
if response.status_code == 201:
    print("Dataset republicado com sucesso!")
    print("Detalhes:", response.json())
else:
    print("Erro ao republicar o dataset:")
    print("Status Code:", response.status_code)
    print("Resposta:", response.text)
