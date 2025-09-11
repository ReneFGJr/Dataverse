import os
import requests
import json
from dotenv import load_dotenv

# Carrega variáveis de ambiente do .env
load_dotenv()

DATAVERSE_URL = os.getenv("DATAVERSE_URL")
API_TOKEN = os.getenv("DATAVERSE_API_TOKEN")


def create_dataset(dataverse_alias, json_file):
    """
    Cria um dataset em um Dataverse específico a partir de um arquivo JSON.

    Args:
        dataverse_alias (str): Alias do Dataverse onde o dataset será criado.
        json_file (str): Caminho para o arquivo JSON com os metadados.

    Returns:
        dict: Resposta da API (JSON).
    """
    url = f"{DATAVERSE_URL}/api/dataverses/{dataverse_alias}/datasets"

    headers = {
        "X-Dataverse-key": API_TOKEN,
        "Content-Type": "application/json"
    }

    # Lê o conteúdo do JSON
    with open(json_file, "r", encoding="utf-8") as f:
        dataset_metadata = json.load(f)

    # Faz a requisição POST
    response = requests.post(url, headers=headers, json=dataset_metadata)

    if response.status_code == 201:
        print("✅ Dataset criado com sucesso!")
    else:
        print(f"⚠️ Erro: {response.status_code} - {response.text}")

    return response.json()
