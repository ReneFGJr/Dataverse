# Customização da Logo - versão 0.24.09.12
# Para a variavel $PAYARA veja Commons/Enviroment
export INSTITUTION='Dataverse'
curl -X PUT -d ", $INSTITUTION" http://localhost:8080/api/admin/settings/:FooterCopyright