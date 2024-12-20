def update_propriety(fileO, fileS):
    # Abrindo e lendo o conteúdo do arquivo principal
    with open(fileO, "r", encoding="utf-8") as file:
        lines = file.readlines()

    # Encontrando a linha que inicia com 'about.TB001'
    start_index = next((i for i, line in enumerate(lines) if line.startswith("about.TB001")), None)

    # Se encontrada, remove o conteúdo a partir dessa linha
    if start_index is not None:
        lines = lines[:start_index]

    # Abrindo e lendo o conteúdo do arquivo adicional
    with open(fileS, "r", encoding="utf-8") as additional_file:
        additional_content = additional_file.readlines()

    # Adicionando o conteúdo do arquivo adicional ao final, preservando UTF-8
    lines.extend(additional_content)

    # Reescrevendo o arquivo principal com o conteúdo atualizado
    with open(fileO, "w", encoding="utf-8") as file:
        file.writelines(lines)

file_path = '/var/www/dataverse/langBundles/Bundle_pt.properties'
additional_file_path = "about_pt.propriety"
update_propriety(file_path, additional_file_path)
print("PORTUGUES - Arquivo atualizado com sucesso!")

file_path = '/var/www/dataverse/langBundles/Bundle_en.properties'
additional_file_path = "about_en.propriety"
update_propriety(file_path, additional_file_path)
print("INGLÊS - Arquivo atualizado com sucesso!")
