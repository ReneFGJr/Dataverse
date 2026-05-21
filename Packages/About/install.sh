cp *.xhtml /usr/local/payara6/glassfish/domains/domain1/applications/dataverse-6.10.1/.
curl -X PUT -d '/IPEN_sobre.xhtml' http://localhost:8080/api/admin/settings/:NavbarAboutUrl