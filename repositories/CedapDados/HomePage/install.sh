#echo "https://guides.dataverse.org/en/latest/installation/config.html?highlight=apitermsofuse"

export PAYARA=/usr/local/payara7/glassfish
export SERVER_URL=http://localhost:8080
export APP=/usr/local/payara7/glassfish/domains/domain1/applications/dataverse-6.11/

export URL=https://cedapdados.ufrgs.br/
export HOME=welcome.xhtml


cp $HOME $APP/$HOME
mkdir $APP/assets/
mkdir $APP/assets/img/
cp *.png $APP/assets/img/.
cp *.jpg $APP/assets/img/.

curl -X PUT -d $APP$HOME $SERVER_URL/api/admin/settings/:HomePageCustomizationFile
