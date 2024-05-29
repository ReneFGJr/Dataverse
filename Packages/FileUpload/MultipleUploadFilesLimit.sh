#Esta configuração controla o número de arquivos que podem ser carregados por meio da IU de uma só vez.
#O padrão é 1000. Deve ser definido como 1 ou superior, pois 0 não tem efeito.
#Para limitar o número de arquivos em um arquivo zip, consulte:ZipUploadFilesLimit

curl -X PUT -d 500 http://localhost:8080/api/admin/settings/:MultipleUploadFilesLimit