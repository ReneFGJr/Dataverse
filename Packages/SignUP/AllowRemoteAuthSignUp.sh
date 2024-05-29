#Esta é uma configuração composta que ativa ou desativa a inscrição em novas contas para métodos de
#autenticação OAuth2 individuais (como Orcid, Google e GitHub).
#Desta forma é possível continuar permitindo logins através de um provedor OAuth2
#para contas já existentes, sem permitir que novos usuários criem contas com este método.

#Por padrão, se a configuração não estiver presente, todas as inscrições OAuth configuradas serão permitidas.
#Se a configuração estiver presente, mas o valor para este método específico não for especificado, presume-se que as inscrições são permitidas para ele.
#Exemplos:

curl -X PUT -d '{"default":"false"}' http://localhost:8080/api/admin/settings/:AllowRemoteAuthSignUp

#…desativa todas as inscrições OAuth.

#curl -X PUT -d '{"default":"true","google":"false"}' http://localhost:8080/api/admin/settings/:AllowRemoteAuthSignUp

#mantém as inscrições abertas para todos os provedores de login OAuth, exceto o Google. (Dito isto, observe que a parte "default":"true" neste exemplo é redundante, pois o padrão seria true de qualquer maneira para todos os métodos, exceto o google.)