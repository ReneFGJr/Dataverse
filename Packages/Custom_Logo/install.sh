# Customização da Logo - versão 0.24.09.12
# Para a variavel $PAYARA veja Commons/Enviroment
export LOGO='logo.png'
export PAYARA='/usr/local/payara7/glassfish'
mkdir $PAYARA/domains/domain1/docroot/logos
mkdir $PAYARA/domains/domain1/docroot/logos/navbar
cp $LOGO $PAYARA/domains/domain1/docroot/logos/navbar/.
curl -X PUT -d '/logos/navbar/$LOGO' http://localhost:8080/api/admin/settings/:LogoCustomizationFile