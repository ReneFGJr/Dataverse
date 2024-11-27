import requests
import json
import os

def adjust_metadata(metadata):
    """
    Ajusta os metadados para corrigir problemas de validação no Dataverse de destino.

    Args:
        metadata (dict): Metadados originais do dataset.

    Returns:
        dict: Metadados ajustados.
    """
    fields = metadata["latestVersion"]["metadataBlocks"]["citation"]["fields"]

    # Verifica e ajusta o campo alternativeTitle
    for field in fields:
        if field["typeName"] == "alternativeTitle" and field["multiple"] is False:
            field["value"] = str(field.get("value", ""))  # Evita erro se o valor estiver ausente

    return metadata

def duplicate_metadata_only(source_base_url, source_doi, target_base_url, target_api_key, local_storage_path="dados"):
    """
    Duplica os metadados de um dataset de um Dataverse para outro, mantendo o mesmo DOI e armazenando os metadados localmente.

    Args:
        source_base_url (str): URL base do Dataverse de origem.
        source_doi (str): DOI do dataset a ser duplicado.
        target_base_url (str): URL base do Dataverse de destino.
        target_api_key (str): Token de API para autenticação no Dataverse de destino.
        local_storage_path (str): Caminho base para armazenar os metadados localmente.

    Returns:
        dict: Resultado da operação com informações sobre o novo dataset.
    """
    headers = {
        "X-Dataverse-key": target_api_key,
        "Content-Type": "application/json"
    }

    # Obter os metadados do dataset original
    print("Obtendo metadados do dataset de origem...")
    source_dataset_url = f"{source_base_url}/api/datasets/:persistentId/?persistentId={source_doi}"
    response = requests.get(source_dataset_url)
    if response.status_code != 200:
        raise Exception(f"Erro ao obter os metadados do dataset de origem: {response.status_code} - {response.text}")

    dataset_metadata = response.json()["data"]
    repository_name = source_base_url.split("//")[-1].split(".")[0]
    dataset_folder = os.path.join(local_storage_path, repository_name, source_doi.replace(":", "_").replace("/", "_"))

    # Criar a pasta para armazenar os metadados localmente
    os.makedirs(dataset_folder, exist_ok=True)

    # Salvar os metadados em um arquivo JSON local
    metadata_file = os.path.join(dataset_folder, "metadata.json")
    with open(metadata_file, "w", encoding="utf-8") as f:
        json.dump(dataset_metadata, f, indent=4, ensure_ascii=False)
    print(f"Metadados salvos em: {metadata_file}")

    # Ajustar os metadados
    print("Ajustando metadados...")
    adjusted_metadata = adjust_metadata(dataset_metadata)

    # Criar o novo dataset no Dataverse de destino
    print("Criando novo Dataset no destino...")
    target_dataset_url = f"{target_base_url}/api/dataverses/root/datasets"
    payload = {
        "datasetVersion": {
            "metadataBlocks": adjusted_metadata["latestVersion"]["metadataBlocks"]
        }
    }  # Removido o uso de 'persistentId' no payload

    print("Enviando requisição para o Dataverse de destino...")
    response = requests.post(target_dataset_url, headers=headers, json=payload)
    if response.status_code != 201:
        raise Exception(f"Erro ao criar o novo dataset no Dataverse de destino: {response.status_code} - {response.text}")

    new_dataset = response.json()["data"]
    print(f"Novo dataset criado com sucesso no Dataverse de destino. ID: {new_dataset['id']}")

    return {"message": "Dataset duplicado com sucesso.", "new_dataset_id": new_dataset["id"]}

# Exemplo de uso
source_base_url = "https://arcadados.fiocruz.br"
source_doi = "doi:10.35078/O6O5TS"  # Ajustado para incluir o prefixo "doi:"
target_base_url = "https://vitrinedadosabertos-dev.rnp.br"
target_api_key = "fc178044-78ff-4bcb-a83d-97eeaee4bbb2"

try:
    result = duplicate_metadata_only(source_base_url, source_doi, target_base_url, target_api_key)
    print(result)
except Exception as e:
    print(f"Erro: {e}")
