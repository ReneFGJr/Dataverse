# Pacote de idioma Dataverse v6.0

Para instalar, dentro do servidor execute install.sh
Antes atribuia privégio de execução
<tt>$ chmod 700 install.sh</tt>


# Alterar o idioma padrão
Arquivo /usr/local/payara7/glassfish/domains/domain1/applications/dataverse/WEB-INF/faces-config.xml

Altere para:
 <application>
        <resource-bundle>
            <base-name>edu.harvard.iq.dataverse.util.LocalBundle</base-name>
            <var>bundle</var>
        </resource-bundle>
        <locale-config>
            <default-locale>pt</default-locale>
            <supported-locale>en</supported-locale>
            <supported-locale>es</supported-locale>
        </locale-config>
    </application>