# Customização da Logo - versão 0.24.09.12
# Para a variavel $PAYARA veja Commons/Enviroment
LOGO='logo.png'
mkdir $PAYARA/domains/domain1/docroot/logos
mkdir $PAYARA/domains/domain1/docroot/logos/navbar
cp img/$LOGO $PAYARA/domains/domain1/docroot/logos/navbar/.
curl -X PUT -d '/logos/navbar/$LOGO' http://localhost:8080/api/admin/settings/:LogoCustomizationFile