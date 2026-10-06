import requests

# ============================================================
# CONFIGURAÇÃO
# ============================================================

DATAVERSE_URL = "http://localhost:8080"

# Se a API administrativa estiver protegida, informe a chave.
API_TOKEN = ""

# Arquivo citation.tsv original da instalação
CITATION_TSV = "citation.tsv"

# Novo assunto
NEW_SUBJECT = "Information Science - Library"


# ============================================================
# CARREGAR O TSV
# ============================================================

def load_tsv():
    with open(CITATION_TSV, "r", encoding="utf-8") as file:
        return file.readlines()


# ============================================================
# LOCALIZAR E ADICIONAR SUBJECT
# ============================================================

def add_subject(lines):
    """
    Procura a seção #controlledVocabulary e acrescenta
    Information Science - Library ao vocabulário subject.
    """

    new_lines = []
    in_vocabulary = False
    subject_exists = False
    last_subject_index = None

    for i, line in enumerate(lines):

        if line.startswith("#controlledVocabulary"):
            in_vocabulary = True

        elif line.startswith("#") and in_vocabulary:
            in_vocabulary = False

        if in_vocabulary:
            columns = line.rstrip("\n").split("\t")

            if len(columns) >= 2 and columns[0] == "subject":

                last_subject_index = len(new_lines)

                # Verifica se já existe
                if NEW_SUBJECT.lower() in [
                    c.lower() for c in columns
                ]:
                    subject_exists = True

        new_lines.append(line)

    if subject_exists:
        print(
            f"O assunto '{NEW_SUBJECT}' já existe."
        )
        return new_lines

    if last_subject_index is None:
        raise RuntimeError(
            "Não foi possível localizar o vocabulário 'subject'."
        )

    # Usa a última linha de subject como modelo
    template = new_lines[last_subject_index]
    columns = template.rstrip("\n").split("\t")

    # ATENÇÃO:
    # normalmente:
    # coluna 0 = DatasetField
    # coluna 1 = Value
    #
    # Ajuste caso seu citation.tsv tenha estrutura diferente.

    columns[0] = "subject"
    columns[1] = NEW_SUBJECT

    new_line = "\t".join(columns) + "\n"

    new_lines.insert(
        last_subject_index + 1,
        new_line
    )

    print(
        f"Novo assunto preparado: {NEW_SUBJECT}"
    )

    return new_lines


# ============================================================
# SALVAR NOVO TSV
# ============================================================

def save_tsv(lines):

    output = "citation_modified.tsv"

    with open(output, "w", encoding="utf-8") as file:
        file.writelines(lines)

    print(f"Arquivo gerado: {output}")

    return output


# ============================================================
# ENVIAR PARA DATAVERSE
# ============================================================

def upload_to_dataverse(filename):

    url = (
        f"{DATAVERSE_URL}"
        "/api/admin/datasetfield/load"
    )

    headers = {
        "Content-Type": "text/tab-separated-values"
    }

    if API_TOKEN:
        headers["X-Dataverse-key"] = API_TOKEN

    with open(filename, "rb") as file:

        response = requests.post(
            url,
            headers=headers,
            data=file
        )

    print("HTTP:", response.status_code)

    try:
        print(response.json())
    except Exception:
        print(response.text)

    response.raise_for_status()


# ============================================================
# MAIN
# ============================================================

def main():

    print("Dataverse - Cadastro de Subject")
    print("--------------------------------")

    lines = load_tsv()

    lines = add_subject(lines)

    filename = save_tsv(lines)

    print()
    print("Enviando configuração para Dataverse...")

    upload_to_dataverse(filename)

    print()
    print(
        f"Subject '{NEW_SUBJECT}' cadastrado."
    )


if __name__ == "__main__":
    main()