mkdir /home/dataverse/payara
chown postgres /home/dataverse/payara
/home/dataverse/stop

/home/dataverse/start
cd /home/dataverse/payara # diretorio onde ficará os arquivos
$PAYARA/bin/asadmin backup-domain --backupdir /home/dataverse/payara domain1
