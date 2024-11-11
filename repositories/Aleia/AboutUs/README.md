:NavbarAboutUrl
Set :NavbarAboutUrl to a fully-qualified URL which will be used for the “About” link in the navbar.

Note: The “About” link will not appear in the navbar until this option is set.

curl -X PUT -d http://dataverse.example.edu http://localhost:8080/api/admin/settings/:NavbarAboutUrl

chmod 700 install.sh

<h1>Guia</h1>
No arquivo Guia_Aleia.pdf está disponível a última versão do Guia do Usuário do Aleia
Versão de 11/out./2023.


/usr/local/payara6/glassfish/domains/domain1/applications/dataverse-6.4/WEB-INF/faces-config.xml

        <locale-config>
            <default-locale>pt</default-locale>
            <supported-locale>en</supported-locale>
            <supported-locale>es</supported-locale>
        </locale-config>
