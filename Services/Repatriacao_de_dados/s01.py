import requests
import json
import os

# Configurações
API_URL = "https://vitrinedadosabertos-dev.rnp.br/api"
API_KEY = "fc178044-78ff-4bcb-a83d-97eeaee4bbb2"
DATAVERSE_ALIAS = "repatriacao"
FILE_JSON = 'dados/arcadados/doi_10.35078_O6O5TS/metadata.json'

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
        # Verificar se "multiple" e "value" estão presentes
        if "multiple" in field and field["multiple"] is False and isinstance(field.get("value"), list):
            field["value"] = field["value"][0] if len(field["value"]) > 0 else ""
        # Verificar se o campo é composto
        if field.get("typeClass") == "compound" and "value" in field:
            fix_metadata_fields(field["value"])

# Preparar os metadados
metadata_blocks = metadata["latestVersion"]["metadataBlocks"]
fix_metadata_fields(metadata_blocks["citation"]["fields"])

# Adicionar o DOI para preservação
metadata_blocks["citation"]["fields"].append({
    "typeName": "identifier",
    "typeClass": "primitive",
    "multiple": False,
    "value": metadata["persistentUrl"]
})

dataset_metadata = {
    "datasetVersion": {
        "metadataBlocks": metadata_blocks
    }
}

# Endpoint para criação do dataset
endpoint = f"{API_URL}/dataverses/{DATAVERSE_ALIAS}/datasets"

# Configuração do cabeçalho
headers = {
    "X-Dataverse-key": API_KEY,
    "Content-Type": "application/json"
}

# Logs para depuração
print("Enviando os seguintes metadados para a API:")
print(json.dumps(dataset_metadata, indent=4, ensure_ascii=False))

# Enviar solicitação para criar o dataset
response = requests.post(endpoint, headers=headers, json=dataset_metadata)

# Verificar resposta
if response.status_code == 201:
    print("Dataset republicado com sucesso!")
    print("Detalhes:", response.json())
else:
    print("Erro ao republicar o dataset:")
    print("Status Code:", response.status_code)
    print("Resposta:", response.text)
