#!/bin/bash

# Defina as variáveis de configuração do Dataverse
API_TOKEN="SEU_API_TOKEN_AQUI"
BASE_URL="https://seu-dataverse-url.com"
HEADERS="X-Dataverse-key:$API_TOKEN"

# Função para adicionar a licença CC-BY
adicionar_licenca() {
  echo "Adicionando a licença CC-BY..."

  DATA=$(cat <<EOF
{
  "name": "CC-BY",
  "uri": "https://creativecommons.org/licenses/by/4.0/",
  "shortDescription": "Atribuição - Permite que outros distribuam, remixem, adaptem e criem obras derivadas, mesmo que para fins comerciais, desde que atribuam crédito apropriado.",
  "active": true
}
EOF
)

  response=$(curl -s -X POST "$BASE_URL/api/admin/licenses" -H "$HEADERS" -H "Content-Type: application/json" -d "$DATA")
  echo "Resposta do servidor: $response"
}

# Função para remover uma licença por ID
remover_licenca() {
  LICENCA_ID=$1
  echo "Removendo licença com ID: $LICENCA_ID..."

  response=$(curl -s -X DELETE "$BASE_URL/api/admin/licenses/$LICENCA_ID" -H "$HEADERS")
  echo "Resposta do servidor: $response"
}

# Função para ativar uma licença por ID
ativar_licenca() {
  LICENCA_ID=$1
  echo "Ativando licença com ID: $LICENCA_ID..."

  DATA='{"active": true}'
  response=$(curl -s -X PUT "$BASE_URL/api/admin/licenses/$LICENCA_ID" -H "$HEADERS" -H "Content-Type: application/json" -d "$DATA")
  echo "Resposta do servidor: $response"
}

# Função principal para selecionar a ação
menu_principal() {
  echo "Selecione a ação que deseja realizar:"
  echo "1) Adicionar licença CC-BY"
  echo "2) Remover licença por ID"
  echo "3) Ativar licença por ID"
  echo "4) Sair"

  read -p "Escolha uma opção (1-4): " opcao

  case $opcao in
    1)
      adicionar_licenca
      ;;
    2)
      read -p "Digite o ID da licença a ser removida: " licenca_id
      remover_licenca $licenca_id
      ;;
    3)
      read -p "Digite o ID da licença a ser ativada: " licenca_id
      ativar_licenca $licenca_id
      ;;
    4)
      echo "Saindo..."
      exit 0
      ;;
    *)
      echo "Opção inválida."
      ;;
  esac
}

# Executa o menu principal
menu_principal
