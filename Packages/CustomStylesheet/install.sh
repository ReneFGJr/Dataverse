FILE = 'custom-stylesheet.css'
mkdir /var/www/dataverse/
mkdir /var/www/dataverse/branding/
cp FILE /var/www/dataverse/branding/.
curl -X PUT -d '/var/www/dataverse/branding/custom-stylesheet.css' http://localhost:8080/api/admin/settings/:StyleCustomizationFile