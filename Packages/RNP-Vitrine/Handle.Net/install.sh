echo "Ativando o Handle"
export PREFIX='20.500.12401'
export PAYARA=/usr/local/payara5/glassfish
export SENHA="ALTERE A SENHA"
export SHOULDER="cedapdados/"

curl -X PUT -d 'hdl' http://localhost:8080/api/admin/settings/:Protocol

curl -X PUT -d 'sequentialNumber' localhost:8080/api/admin/settings/:IdentifierGenerationStyle
#curl -X PUT -d 'randomString' localhost:8080/api/admin/settings/:IdentifierGenerationStyle

#curl -X PUT -d 'DEPENDENT' localhost:8080/api/admin/settings/:DataFilePIDFormat
curl -X PUT -d 'INDEPENDENT' localhost:8080/api/admin/settings/:DataFilePIDFormat

curl -X PUT -d $PREFIX http://localhost:8080/api/admin/settings/:Authority

curl -X PUT -d $SHOULDER http://localhost:8080/api/admin/settings/:Shoulder

echo "Atribui DOI para cada dataset, sem gerar para arquivos"

curl -X PUT -d 'true' http://localhost:8080/api/admin/settings/:FilePIDsEnabled
#curl -X PUT -d 'false' http://localhost:8080/api/admin/settings/:FilePIDsEnabled


echo "Enviando Parametros"
$PAYARA/bin/asadmin create-jvm-options '-Ddataverse.handlenet.admcredfile=/hs/svr_2/admpriv.bin'
$PAYARA/bin/asadmin create-jvm-options '-Ddataverse.handlenet.admprivphrase=$SENHA'
$PAYARA/bin/asadmin create-jvm-options '-Ddataverse.handlenet.index=300'

mkdir /hs
mkdir /hs/srv_2/
echo "Copiando Arquivo"
cp admpriv.bin /hs/svr_2/admpriv.bin

echo "Criando sequencia de Registros"
echo "Execute os comandos abaixo:"
echo "sudo postgres"
echo "psql dvndb"
echo "\i createsequence.sql"
echo "\q"