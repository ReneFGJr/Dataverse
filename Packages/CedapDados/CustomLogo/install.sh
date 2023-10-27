export LOGO='logo_cedapdados'
mkdir /usr/local/payara5/glassfish/domains/domain1/docroot/logos/
mkdir /usr/local/payara5/glassfish/domains/domain1/docroot/logos/navbar/
cp *.png /usr/local/payara5/glassfish/domains/domain1/docroot/logos/navbar/.

curl -X PUT -d '/logos/navbar/$LOGO' http://localhost:8080/api/admin/settings/:LogoCustomizationFile