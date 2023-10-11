#echo "https://guides.dataverse.org/en/latest/installation/config.html?highlight=apitermsofuse"

export PAYARA=/usr/local/payara5/glassfish
export SERVER_URL=http://localhost:8080
export URL=https://aleia.ibict.br/
export ABOUT_XML=about.xhtml
export FAQ_XML=faq.xhtml
export APP=/usr/local/payara5/glassfish/domains/domain1/applications/dataverse-5.12.1/

cp $ABOUT_XML $APP/$ABOUT_XML
curl -X PUT -d $URL$ABOUT_XML $SERVER_URL/api/admin/settings/:NavbarAboutUrl

#Reinicia o Dataverse
/home/dataverse/restart