def atualizar_bundle(file_about, file_bundle):
    import os

    # Verificar se os arquivos existem
    if not os.path.exists(file_about) or not os.path.exists(file_bundle):
        print("Um ou ambos os arquivos especificados não existem.")
        return

    # Ler o conteúdo de about_br.properties
    with open(file_about, 'r', encoding='utf-8') as about_file:
        about_lines = about_file.readlines()

    # Criar um dicionário para as variáveis de about_br.properties
    about_dict = {}
    for line in about_lines:
        line = line.strip()
        if "=" in line:
            key, value = line.split("=", 1)
            about_dict[key.strip()] = value.strip()

    # Ler o conteúdo de Bundle.properties e atualizar ou adicionar as variáveis
    with open(file_bundle, 'r+', encoding='utf-8') as bundle_file:
        bundle_lines = bundle_file.readlines()

        # Criar um dicionário para as variáveis já existentes em Bundle.properties
        bundle_dict = {}
        for line in bundle_lines:
            line = line.strip()
            if "=" in line:
                key, value = line.split("=", 1)
                bundle_dict[key.strip()] = value.strip()

        # Atualizar ou adicionar as variáveis
        for key, value in about_dict.items():
            if key in bundle_dict:
                # Atualizar a variável existente
                bundle_dict[key] = value
            else:
                # Adicionar nova variável
                bundle_dict[key] = value

        # Reescrever o conteúdo de Bundle.properties
        bundle_file.seek(0)
        bundle_file.truncate()  # Limpar o conteúdo antigo
        for key, value in bundle_dict.items():
            bundle_file.write(f"{key}={value}\n")

    print("Bundle.propriety atualizado com sucesso.")

# Exemplo de uso:
fileO = 'about_pt.propriety'
fileD = '/var/www/dataverse/langBundles/Bundle_pt.properties'
atualizar_bundle(fileO, fileD)
