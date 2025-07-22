echo "habilita a autenticação remota - ORCID"
curl -X PUT -d '{"default":"true"}' http://localhost:8080/api/admin/settings/:AllowRemoteAuthSignUp