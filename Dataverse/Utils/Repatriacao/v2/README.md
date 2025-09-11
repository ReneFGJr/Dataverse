$SERVER_URL/api/dataverses/$PARENT/datasets/:import?pid=doi:$DOI&release=no&doNotValidate=true

curl -X PUT -d true http://localhost:8080/api/admin/settings/:AllowImportIdentifier
