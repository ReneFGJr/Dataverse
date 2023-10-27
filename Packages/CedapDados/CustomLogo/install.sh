export LOGO='logo_cedapdados.png'
mkdir /usr/local/payara5/glassfish/domains/domain1/docroot/logos/
mkdir /usr/local/payara5/glassfish/domains/domain1/docroot/logos/navbar/
cp *.png /usr/local/payara5/glassfish/domains/domain1/docroot/logos/navbar/.

curl -X PUT -d '/logos/navbar/logo_cedapdados.png' http://localhost:8080/api/admin/settings/:LogoCustomizationFile