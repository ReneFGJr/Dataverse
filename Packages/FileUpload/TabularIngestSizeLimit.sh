#Limite em bytes para limitar a tentativa de “ingestão” ou não de arquivos tabulares
#(que podem consumir muitos recursos). Por exemplo, com o seguinte em vigor,
#arquivos com tamanho superior a 2 GB não passarão pelo processo de ingestão:


curl -X PUT -d 2000000000 http://localhost:8080/api/admin/settings/:TabularIngestSizeLimit

#Você pode substituir essa configuração global por formato para os seguintes formatos:
#DTA
#POR
#SAV
#Dados Rdados
#CSV
#XLSX (em minúsculas)

#Ex:
#curl -X PUT -d 1000000 http://localhost:8080/api/admin/settings/:TabularIngestSizeLimit:Rdata