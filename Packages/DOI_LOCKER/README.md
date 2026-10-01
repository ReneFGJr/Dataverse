# Desbloqueio de um trabalho no Dataverse

Este procedimento utiliza o comando fornecido para remover o bloqueio do tipo `finalizePublication` de um trabalho (dataset) no Dataverse do IPEN.

## Antes de executar

- Tenha o `curl` instalado e uma chave de API de administrador do Dataverse.
- Confirme o DOI do trabalho que deseja desbloquear.
- Confirme que a finalização da publicação não está mais em andamento antes de remover o bloqueio.

## Como desbloquear

1. Substitua `[API do ADMIN]` pela chave de API do administrador, sem os colchetes.
2. Substitua `doi:10.58148/IPEN/VSVE6E` pelo DOI do trabalho desejado, se necessário.
3. Execute o comando no terminal:

```bash
curl -sS -X DELETE -H "X-Dataverse-key: [API do ADMIN]" "https://datarepository.ipen.br/api/datasets/:persistentId/locks?persistentId=doi:10.58148/IPEN/VSVE6E&type=finalizePublication"
```

No Windows PowerShell, use `curl.exe` no lugar de `curl` para chamar o executável.

Mantenha `:persistentId` literalmente no caminho da URL. O DOI é informado no parâmetro `persistentId`, após o `?`. Mantenha também as aspas ao redor da URL, pois ela contém `&`.

## O que o comando faz

| Parte | Finalidade |
| --- | --- |
| `-sS` | Oculta o indicador de progresso e exibe erros do curl. |
| `-X DELETE` | Solicita a remoção do bloqueio. |
| `X-Dataverse-key` | Envia a chave de API do administrador. |
| `persistentId=doi:10.58148/IPEN/VSVE6E` | Identifica o trabalho pelo DOI. |
| `type=finalizePublication` | Especifica o tipo de bloqueio a remover. |

O alvo da requisição é o bloqueio do trabalho; a operação não é uma solicitação de exclusão do dataset.

## Verificação

Confira a resposta da API e acesse novamente o trabalho no Dataverse para verificar se o bloqueio foi removido e se a operação desejada está disponível. A remoção do bloqueio, por si só, não confirma que a publicação foi concluída.

Se precisar visualizar o status HTTP, acrescente `-i` ao comando. A opção `-sS` não faz o curl tratar respostas HTTP de erro como falhas de execução; confira também o conteúdo da resposta.

Caso o desbloqueio falhe, verifique a chave de API, as permissões do administrador, o DOI informado e a mensagem retornada pela API.

Não salve a chave real neste README nem a inclua em commits ou capturas de tela.
