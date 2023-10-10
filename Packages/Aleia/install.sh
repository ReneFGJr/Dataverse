export PAYARA=/usr/local/payara5/glassfish
export SERVER_URL=http://localhost:8080
curl "$SERVER_URL/api/info/apiTermsOfUse"

#curl -X PUT -d false http://localhost:8080/api/admin/settings/:AllowCustomTermsOfUse


:ApplicationTermsOfUse
Upload an default language HTML file containing the Terms of Use to be displayed at sign up. Supported HTML tags are listed under the Dataset + File Management section of the User Guide.

curl -X PUT -d@UserTerm.html http://localhost:8080/api/admin/settings/:ApplicationTermsOfUse

To upload a language specific Terms of Use file,

curl -X PUT -d@UserTerm.html_en.html http://localhost:8080/api/admin/settings/:ApplicationTermsOfUse/lang/fr

To delete language specific option,

curl -X DELETE http://localhost:8080/api/admin/settings/:ApplicationTermsOfUse/lang/fr
