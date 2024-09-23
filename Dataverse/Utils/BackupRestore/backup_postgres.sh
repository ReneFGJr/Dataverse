mkdir /home/postgres/backup
chown postgres /home/dataverse/backup -R
su - postgres
cd /home/dataverse/backup # diretorio onde ficará os arquivos
pg_dump dvndb > dvndb.sql