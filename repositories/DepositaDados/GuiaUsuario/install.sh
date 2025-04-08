#https://aleia.ibict.br/guide/guiaUsuarioBr.pdf

# Defina o caminho da instalação do Payara
export PAYARA=/usr/local/payara6/glassfish
echo "PAYARA=$PAYARA"

echo "Copiando guide"
cp guide.xhtml $PAYARA/domains/domain1/applications/dataverse-6.4/.
echo "Criando Diretorio"
mkdir -p $PAYARA/domains/domain1/docroot/guide

echo "Copiando Arquivos"
cp guiaUsuarioBr.pdf /$PAYARA/domains/domain1/docroot/guide/guiaUsuarioBr.pdf
cp guiaUsuarioBr.pdf /$PAYARA/domains/domain1/docroot/guide/guiaUsuarioBr.pdf
cp guiaUsuarioBr.pdf /usr/local/payara6/glassfish/domains/domain1/applications/dataverse-6.4/.
cp guiaUsuarioBr.pdf /var/www/guide/public/

echo "Configurando GuidePage"
curl -X PUT -d /guide.xhtml http://localhost:8080/api/admin/settings/:NavbarGuidesUrl
