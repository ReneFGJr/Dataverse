#Habilita ou desabilida o cadastro de novos usuários

curl -X PUT -d 'false' http://localhost:8080/api/admin/settings/:AllowSignUp
#false - desabilita
#true - habilita