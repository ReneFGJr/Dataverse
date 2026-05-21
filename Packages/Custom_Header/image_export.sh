# Customização da Logo - versão 0.24.09.12
# Para a variavel $PAYARA veja Commons/Enviroment
export LOGO='*.png'
export PAYARA='/usr/local/payara7/glassfish'
mkdir $PAYARA/domains/domain1/docroot/logos
mkdir $PAYARA/domains/domain1/docroot/logos/navbar
cp $LOGO $PAYARA/domains/domain1/docroot/logos/navbar/.
