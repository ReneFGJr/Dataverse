## Para visualizar áreas existentes
 curl -s http://localhost:8080/api/metadatablocks/citation | jq '.data.fields[] | select(.name=="subject")'

## Para incluir, editr o arquivo citation.tsv

## Atualizar
 python3 citation.py
