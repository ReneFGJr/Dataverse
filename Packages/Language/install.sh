echo "Criar Pastas"
mkdir /var/
mkdir /var/www/
mkdir /var/www/dataverse/
mkdir /var/www/dataverse/langBundles

export PAYARA=/usr/local/payara6/glassfish

echo "Criando parametro para o Payara"
$PAYARA/bin/asadmin create-jvm-options '-Ddataverse.lang.directory=/var/www/dataverse/langBundles'
$PAYARA/bin/asadmin stop-domain

echo "Enviando Arquivo"
$PAYARA/bin/asadmin start-domain

clear
echo "Aguarde o servidor voltar do Dataverse, e pressione [ENTER]"
read -n 1 -s
echo "Continuando..."

curl http://localhost:8080/api/admin/datasetfield/loadpropertyfiles -X POST --upload-file languages.zip -H "Content-Type: application/zip"
$PAYARA/bin/asadmin stop-domain

echo "Definindo os idiomas ativos"
$PAYARA/bin/asadmin start-domain
clear
echo "Aguarde o servidor voltar do Dataverse, e pressione [ENTER]"
read -n 1 -s
echo "Continuando..."
echo "===>Definindo os idiomas do Dataverse e suas extensões"
curl http://localhost:8080/api/admin/settings/:Languages -X PUT -d '[{"locale":"pt","title":"Português"}, {"locale":"en","title":"English"}, {"locale":"es","title":"Espanhol"}]'
$PAYARA/bin/asadmin stop-domain

echo "Reinicializando"
$PAYARA/bin/asadmin start-domain