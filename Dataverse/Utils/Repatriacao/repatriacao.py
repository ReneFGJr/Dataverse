import requests
import os

# Definir as URLs das APIs e os APIKEYs
OLD_DATAVERSE_API_URL = 'https://vitrinedadosabertos-dev.rnp.br/api'
NEW_DATAVERSE_API_URL = 'https://vitrinedadosabertos-dev.rnp.br/api'
OLD_APIKEY = 'fc178044-78ff-4bcb-a83d-97eeaee4bbb2'
NEW_APIKEY = 'fc178044-78ff-4bcb-a83d-97eeaee4bbb2'

# Função para baixar os metadados de um dataset
def download_dataset_metadata(dataset_id):
    #url = f"{OLD_DATAVERSE_API_URL}/datasets/{dataset_id}"
    url = f"{OLD_DATAVERSE_API_URL}/datasets/:persistentId/versions/:draft/files?persistentId={dataset_id}"
    url = f"https://vitrinedadosabertos-dev.rnp.br/api/datasets/export?exporter=json&persistentId=doi%3A10.5072/FK2/TNSIFQ"
    url = f"https://vitrinedadosabertos-dev.rnp.br/api/datasets/export?exporter=schema.org&persistentId=doi%3A10.5072/FK2/TNSIFQ"
    headers = {'X-Dataverse-key': OLD_APIKEY}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"#001# Erro ao baixar metadados do dataset: {response.status_code}")
        return None

# Função para baixar os arquivos do dataset
def download_dataset_files(dataset_id, download_path):
    #url = f"{OLD_DATAVERSE_API_URL}/datasets/{dataset_id}/versions/:latest/files"
    url = f"{OLD_DATAVERSE_API_URL}/:persistentId/versions/:draft/files?persistentId={dataset_id}"
    headers = {'X-Dataverse-key': OLD_APIKEY}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        files = response.json().get('data')
        for file in files:
            file_id = file['dataFile']['id']
            file_url = f"{OLD_DATAVERSE_API_URL}/access/datafile/{file_id}"
            file_response = requests.get(file_url, headers=headers)

            if file_response.status_code == 200:
                file_name = file['dataFile']['filename']
                file_path = os.path.join(download_path, file_name)
                with open(file_path, 'wb') as f:
                    f.write(file_response.content)
                print(f"Arquivo {file_name} baixado com sucesso.")
            else:
                print(f"Erro ao baixar arquivo {file_id}: {file_response.status_code}")
    else:
        print(f"Erro ao listar arquivos do dataset: {response.status_code}")

# Função para fazer o upload dos metadados em um novo Dataverse
def upload_dataset_metadata(metadata, new_dataverse_alias):
    url = f"{NEW_DATAVERSE_API_URL}/dataverses/{new_dataverse_alias}/datasets"
    headers = {
        'X-Dataverse-key': NEW_APIKEY,
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, json=metadata)

    if response.status_code == 201:
        print("#200 - Metadados submetidos com sucesso.")
        return response.json()
    else:
        print(f"#400 - Erro ao submeter metadados: {response.status_code}")
        print(response.json())
        return None

# Função para fazer o upload dos arquivos em um novo Dataverse
def upload_files_to_dataset(dataset_id, upload_path):
    files = os.listdir(upload_path)
    for file_name in files:
        file_path = os.path.join(upload_path, file_name)
        url = f"{NEW_DATAVERSE_API_URL}/datasets/{dataset_id}/add"
        headers = {'X-Dataverse-key': NEW_APIKEY}
        files = {'file': open(file_path, 'rb')}
        response = requests.post(url, headers=headers, files=files)

        if response.status_code == 200:
            print(f"Arquivo {file_name} enviado com sucesso.")
        else:
            print(f"Erro ao enviar arquivo {file_name}: {response.status_code}")

# Função principal
def main():
    # ID do dataset no Dataverse antigo e novo alias para o Dataverse
    old_dataset_id = 'doi:10.5072/FK2/XQD31T'
    new_dataverse_alias = 'testesinep'
    download_path = 'dataset_files'

    # Baixar os metadados e arquivos
    os.makedirs(download_path, exist_ok=True)
    metadata = download_dataset_metadata(old_dataset_id)
    download_dataset_files(old_dataset_id, download_path)

    # Submeter os metadados ao novo Dataverse
    if metadata:
        new_dataset = upload_dataset_metadata(metadata, new_dataverse_alias)
        if new_dataset:
            new_dataset_id = new_dataset['data']['id']

            # Fazer upload dos arquivos ao novo dataset
            upload_files_to_dataset(new_dataset_id, download_path)

if __name__ == '__main__':
    main()
