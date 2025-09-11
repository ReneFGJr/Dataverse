import os
import requests
from dotenv import load_dotenv

# Carrega as variáveis do .env
load_dotenv()

DATAVERSE_URL = os.getenv("DATAVERSE_URL")
API_TOKEN = os.getenv("DATAVERSE_API_TOKEN")
CONTACT_EMAIL = os.getenv("DATAVERSE_CONTACT_EMAIL")


def create_dataverse(dataverse_alias, name, affiliation="", description=""):
    """
    Cria um Dataverse dentro do root no servidor Dataverse informado.
    """

    url = f"{DATAVERSE_URL}/api/dataverses/root"

    headers = {
        "X-Dataverse-key": API_TOKEN,
        "Content-Type": "application/json"
    }

    payload = {
        "alias": dataverse_alias,
        "name": name,
        "affiliation": affiliation,
        "dataverseContacts": [{
            "contactEmail": CONTACT_EMAIL
        }],
        "description": description
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 201:
        print("✅ Dataverse criado com sucesso!")
    else:
        print(f"⚠️ Erro: {response.status_code} - {response.text}")

    return response.json()
