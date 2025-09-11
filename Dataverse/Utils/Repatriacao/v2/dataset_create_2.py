import os
import requests
import json
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do .env
load_dotenv()

DATAVERSE_URL = os.getenv("DATAVERSE_URL")
API_TOKEN = os.getenv("DATAVERSE_API_TOKEN")


def update_dataset(persistent_id, json_file):
    """
    Atualiza um dataset existente mantendo o mesmo DOI (cria nova versão de rascunho).

    Args:
        persistent_id (str): DOI ou Handle do dataset (ex.: "doi:10.1234/abcd").
        json_file (str): Caminho para o arquivo JSON com os novos metadados.

    Returns:
        dict: Resposta da API (JSON).
    """
    url = f"{DATAVERSE_URL}/api/datasets/:persistentId/versions/:draft"
    params = {"persistentId": persistent_id}
    headers = {
        "X-Dataverse-key": API_TOKEN,
        "Content-Type": "application/json"
    }

    # Lê o JSON com os novos metadados
    with open(json_file, "r", encoding="utf-8") as f:
        dataset_metadata = json.load(f)

    # Envia a atualização
    response = requests.put(url,
                            headers=headers,
                            params=params,
                            json=dataset_metadata)

    if response.status_code == 200:
        print("✅ Dataset atualizado com sucesso (versão em rascunho).")
    else:
        print(f"⚠️ Erro: {response.status_code} - {response.text}")

    return response.json()
