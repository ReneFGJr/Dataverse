from pathlib import Path


def update_propriety(fileO, fileS):
    main_file = Path(fileO)
    additional_file = Path(fileS)

    if not main_file.exists():
        print(f"Arquivo principal não encontrado: {main_file}")
        return False

    if not additional_file.exists():
        print(f"Arquivo adicional não encontrado: {additional_file}")
        return False

    # Abrindo e lendo o conteúdo do arquivo principal
    with open(main_file, "r", encoding="utf-8") as file:
        lines = file.readlines()

    # Encontrando a linha que inicia com 'about.TB001'
    start_index = next((i for i, line in enumerate(lines) if line.startswith("about.TB001")), None)

    # Se encontrada, remove o conteúdo a partir dessa linha
    if start_index is not None:
        lines = lines[:start_index]

    # Abrindo e lendo o conteúdo do arquivo adicional
    with open(additional_file, "r", encoding="utf-8") as file:
        additional_content = file.readlines()

    # Adicionando o conteúdo do arquivo adicional ao final, preservando UTF-8
    lines.extend(additional_content)

    # Reescrevendo o arquivo principal com o conteúdo atualizado
    with open(main_file, "w", encoding="utf-8") as file:
        file.writelines(lines)

    return True

file_path = '/var/www/dataverse/langBundles/Bundle_pt.properties'
additional_file_path = "about_pt.propriety"
if update_propriety(file_path, additional_file_path):
    print("PORTUGUES - Arquivo atualizado com sucesso!")

file_path = '/var/www/dataverse/langBundles/Bundle_en.properties'
additional_file_path = "about_en.propriety"
if update_propriety(file_path, additional_file_path):
    print("INGLÊS - Arquivo atualizado com sucesso!")
