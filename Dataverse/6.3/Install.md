Oracle Linux Server

 sudo yum update

==Instalação do ZIP==
sudo yum install zip

==Instalação do LYNX==
sudo yum install lynx

==Instalação do Nano==
 sudo yum install nano

=Java 17=
sudo yum install java-17-openjdk

java -v

=Postgres 14=
sudo rpm --import https://download.postgresql.org/pub/repos/yum/RPM-GPG-KEY-PGDG
sudo nano /etc/yum.repos.d/pgdg.repo

=Postgres 14=
yum install -y https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm
yum makecache fast
yum install -y postgresql13-server
/usr/pgsql-13/bin/postgresql-13-setup initdb
/usr/bin/systemctl start postgresql-13
/usr/bin/systemctl enable postgresql-13

Copiar o código
 [pgdg14]
 name=PostgreSQL 14 for RHEL/CentOS $releasever - $basearch
 baseurl=https://download.postgresql.org/pub/repos/yum/14/redhat/rhel-$releasever-$basearch
 enabled=1
 gpgcheck=0
