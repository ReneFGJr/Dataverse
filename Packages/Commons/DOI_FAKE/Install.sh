


curl http://localhost:8080/api/admin/settings/:DoiProvider -X PUT -d FAKE_DOI_PROVIDER=true

echo "Atribui DOI para cada dataset, sem gerar para arquivos"
curl -X PUT -d 'false' http://localhost:8080/api/admin/settings/:FilePIDsEnabled