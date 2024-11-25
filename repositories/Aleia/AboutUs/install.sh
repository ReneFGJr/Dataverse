#echo "https://guides.dataverse.org/en/latest/installation/config.html?highlight=apitermsofuse"

export PAYARA=/usr/local/payara6/glassfish
export SERVER_URL=http://localhost:8080
export URL=https://aleia.ibict.br/
export ABOUT_XML=about.xhtml
export FAQ_XML=faq.xhtml
export APP=/usr/local/payara6/glassfish/domains/domain1/applications/dataverse-6.4
export GUIDE=Guia_Aleia.pdf
export IMG=*.png

cp $ABOUT_XML $APP/$ABOUT_XML
cp $FAQ_XML $APP/$FAQ_XML
mkdir $APP/assets/
mkdir $APP/assets/pdf/
mkdir $APP/assets/img/
cp $GUIDE $APP/assets/pdf/$GUIDE
cp $IMG $APP/assets/img/.

curl -X PUT -d $ABOUT_XML $SERVER_URL/api/admin/settings/:NavbarAboutUrl

#Reinicia o Dataverse
/home/dataverse/restart