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
            field["value"] = str(field["value"])  # Converte para string, caso seja interpretado como múltiplo

    return metadata

def download_dataset(source_base_url, source_doi, local_storage_path="dados"):

    # Obter os metadados do dataset original
    source_dataset_url = f"{source_base_url}/api/datasets/:persistentId/?persistentId={source_doi}"
    print(f"Carregando dados da URL\n{source_base_url}")
    response = requests.get(source_dataset_url)
    if response.status_code != 200:
        raise Exception(f"Erro ao obter os metadados do dataset de origem: {response.text}")

    dataset_metadata = response.json()["data"]
    repository_name = source_base_url.split("//")[-1].split(".")[0]
    dataset_folder = os.path.join(local_storage_path, repository_name, source_doi.replace(":", "_").replace("/", "_"))

    # Criar a pasta para armazenar os metadados localmente
    print("Criando diretórios")
    os.makedirs(dataset_folder, exist_ok=True)

    print("Salvando metadados na pasta")
    # Salvar os metadados em um arquivo JSON local
    metadata_file = os.path.join(dataset_folder, "metadata.json")
    with open(metadata_file, "w", encoding="utf-8") as f:
        json.dump(dataset_metadata, f, indent=4, ensure_ascii=False)
    print(f"Metadados salvos em: {metadata_file}")


# Exemplo de uso
source_base_url = "https://arcadados.fiocruz.br"
source_doi = "doi:10.35078/O6O5TS"  # Ajustado para incluir o prefixo "doi:"

try:
    result = download_dataset(source_base_url, source_doi)
    print(result)
except Exception as e:
    print(f"Erro: {e}")
