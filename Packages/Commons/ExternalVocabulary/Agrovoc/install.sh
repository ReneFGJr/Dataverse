mkdir /usr/local/payara6/glassfish/domains/domain1/applications/dataverse-6.1/cvoc/
mkdir /usr/local/payara6/glassfish/domains/domain1/applications/dataverse-6.1/cvoc/js
cp skosmos.js /usr/local/payara6/glassfish/domains/domain1/applications/dataverse-6.1/cvoc/js/.
cp ../cvocutils.js /usr/local/payara6/glassfish/domains/domain1/applications/dataverse-6.1/cvoc/js/.
curl -X PUT --upload-file agrovoc.json http://localhost:8080/api/admin/settings/:CVocConf