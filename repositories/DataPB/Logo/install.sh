# Para a variavel $PAYARA veja Commons/Enviroment
LOGO=''
mkdir $PAYARA/domains/domain1/docroot/logos
mkdir $PAYARA/domains/domain1/docroot/logos/navbar
cp ing/logo.png $PAYARA/domains/domain1/docroot/logos/navbar/.
curl -X PUT -d '/logos/navbar/logo.png' http://localhost:8080/api/admin/settings/:LogoCustomizationFile