#echo "https://guides.dataverse.org/en/latest/installation/config.html?highlight=apitermsofuse"

export PAYARA=/usr/local/payara5/glassfish
export SERVER_URL=http://localhost:8080
export URL=https://depositadados.ibict.br/
export ABOUT_XML=about.xhtml
export FAQ_XML=faq.xhtml
export APP=/usr/local/payara5/glassfish/domains/domain1/applications/dataverse/
export GUIDE=Guia_Aleia.pdf
export IMG=fluxo_deposito.png

cp $ABOUT_XML $APP/$ABOUT_XML
cp $FAQ_XML $APP/$FAQ_XML
mkdir $APP/assets/
mkdir $APP/assets/pdf/
mkdir $APP/assets/img/
cp $GUIDE $APP/assets/pdf/$GUIDE
cp $IMG $APP/assets/img/$IMG

curl -X PUT -d $URL$ABOUT_XML $SERVER_URL/api/admin/settings/:NavbarAboutUrl

#Reinicia o Dataverse
/home/dataverse/restart