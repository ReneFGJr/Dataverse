#Por motivos de desempenho, a instalação do Dataverse permitirá apenas a criação de arquivos zip de até 100 MB,
#mas o limite pode ser aumentado. Aqui está um exemplo de aumento do limite para 1 GB:
#
#Na IU, os usuários que tentarem baixar um arquivo zip maior que o :ZipDownloadLimit
#da instalação do Dataverse receberão mensagens informando que o arquivo zip é muito grande e
#serão apresentadas ao usuário opções alternativas de acesso.

curl -X PUT -d 1000000000 http://localhost:8080/api/admin/settings/:ZipDownloadLimit
