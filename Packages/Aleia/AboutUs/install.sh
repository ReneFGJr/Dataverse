#echo "https://guides.dataverse.org/en/latest/installation/config.html?highlight=apitermsofuse"

export PAYARA=/usr/local/payara5/glassfish
export SERVER_URL=http://localhost:8080
export URL=https://aleia.ibict.br/About.hxml
export ABOUT_XML=Aboutus.xml

curl -X PUT -d $URL$ABOUT_XML $SERVER_URL/api/admin/settings/:NavbarAboutUrl
