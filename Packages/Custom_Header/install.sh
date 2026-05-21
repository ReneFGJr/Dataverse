cp custom-header.html /var/www/dataverse/branding/custom-header.html
curl -X PUT -d '/var/www/dataverse/branding/custom-header.html' http://localhost:8080/api/admin/settings/:HeaderCustomizationFile