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
    Adiciona 'Information Science - Library' ao vocabulário
    controlado do campo subject do citation.tsv.
    """

    NEW_VALUE = "Information Science - Library"
    NEW_IDENTIFIER = "information_science_library"

    # -------------------------------------------------------
    # Descobrir cabeçalho do vocabulário controlado
    # -------------------------------------------------------

    header_index = None
    header = None

    for i, line in enumerate(lines):
        cols = line.rstrip("\n").split("\t")

        # Procura uma tabela que tenha DatasetField e Value
        if "DatasetField" in cols and "Value" in cols:
            header_index = i
            header = cols

            print("Cabeçalho encontrado:")
            print(header)
            break

    if header_index is None:
        raise RuntimeError(
            "Não foi possível localizar o cabeçalho "
            "do vocabulário controlado no citation.tsv."
        )

    # -------------------------------------------------------
    # Descobrir posições das colunas
    # -------------------------------------------------------

    field_col = header.index("DatasetField")
    value_col = header.index("Value")

    identifier_col = None
    display_order_col = None

    if "identifier" in header:
        identifier_col = header.index("identifier")

    if "displayOrder" in header:
        display_order_col = header.index("displayOrder")

    # -------------------------------------------------------
    # Localizar todos os valores de subject
    # -------------------------------------------------------

    subject_rows = []

    for i in range(header_index + 1, len(lines)):

        line = lines[i]

        # Próxima seção
        if line.startswith("#"):
            if subject_rows:
                break
            continue

        cols = line.rstrip("\n").split("\t")

        if len(cols) <= max(field_col, value_col):
            continue

        if cols[field_col].strip() == "subject":

            subject_rows.append({
                "index": i,
                "columns": cols
            })

            print(
                "Subject encontrado:",
                cols[value_col]
            )

    if not subject_rows:
        raise RuntimeError(
            "O campo 'subject' foi localizado no cabeçalho, "
            "mas nenhum valor do vocabulário foi encontrado."
        )

    # -------------------------------------------------------
    # Verificar se já existe
    # -------------------------------------------------------

    for row in subject_rows:

        cols = row["columns"]

        if cols[value_col].strip().lower() == NEW_VALUE.lower():

            print(
                f"\n'{NEW_VALUE}' já está cadastrado."
            )

            return lines

    # -------------------------------------------------------
    # Criar nova linha
    # -------------------------------------------------------

    last_row = subject_rows[-1]

    # Número de colunas igual ao cabeçalho
    new_cols = [""] * len(header)

    new_cols[field_col] = "subject"
    new_cols[value_col] = NEW_VALUE

    # Identificador próprio
    if identifier_col is not None:
        new_cols[identifier_col] = NEW_IDENTIFIER

    # Ordem
    if display_order_col is not None:

        orders = []

        for row in subject_rows:

            cols = row["columns"]

            if len(cols) > display_order_col:

                try:
                    orders.append(
                        int(cols[display_order_col])
                    )
                except ValueError:
                    pass

        if orders:
            new_cols[display_order_col] = str(max(orders) + 1)

    # -------------------------------------------------------
    # Inserir depois do último subject
    # -------------------------------------------------------

    new_line = "\t".join(new_cols) + "\n"

    insert_position = last_row["index"] + 1

    lines.insert(
        insert_position,
        new_line
    )

    print()
    print("Novo Subject:")
    print(NEW_VALUE)

    if identifier_col is not None:
        print(
            "Identifier:",
            NEW_IDENTIFIER
        )

    print(
        "Inserido na linha:",
        insert_position + 1
    )

    return lines


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