echo "Iniciando backup do Payara Server e do banco de dados dvndb..."
mkdir /home/dataverse/backup
chown postgres /home/dataverse/backup
sudo -u postgres pg_dump dvndb > dvndb_$(date +%Y%m%d).sql

echo "Backup do banco de dados dvndb realizado com sucesso."
/home/dataverse/stop
cd /home/dataverse/backup # diretorio onde ficará os arquivos
export PAYARA=/usr/local/payara6/glashfish
$PAYARA/bin/asadmin backup-domain --backupdir /home/dataverse/backup domain1
/home/dataverse/start
