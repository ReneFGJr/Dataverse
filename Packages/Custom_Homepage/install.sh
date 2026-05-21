mkdir -p /var/www/dataverse/branding
cp custom-homepage.html /var/www/dataverse/branding/custom-homepage.html
curl -X PUT -d '/var/www/dataverse/branding/custom-homepage.html' http://localhost:8080/api/admin/settings/:HomePageCustomizationFile