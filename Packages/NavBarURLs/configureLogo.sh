echo "Configurando o logo"
curl -X PUT -d '/logos/navbar/logo.png' http://localhost:8080/api/admin/settings/:LogoCustomizationFile

#Para remover
#curl -X DELETE http://localhost:8080/api/admin/settings/:LogoCustomizationFile