# Limite o número de arquivos em um zip que a instalação do Dataverse aceitará.
# Na ausência desta configuração, a instalação do Dataverse tem como padrão um limite de 1.000 arquivos por arquivo zip.

curl -X PUT -d 2048 http://localhost:8080/api/admin/settings/:ZipUploadFilesLimit