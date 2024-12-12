echo "ACESSANDO A PASTA DE CONFIGURACOES"
chmod +x update-fields.sh

echo "CARREGANDO A ATUALIZACAO DO SCHEMA"
curl http://localhost:8080/api/admin/datasetfield/load -X POST --data-binary @Term.tsv -H "Content-type: text/tab-separated-values"


echo "CARREGANDO SCHEMA"
rm schema.xml -r
curl "http://localhost:8080/api/admin/index/solr/schema" > schema.xml


echo "ATUALIZANDO O SCHEMA - ver a versão"
cat schema.xml | ./update-fields.sh /usr/local/solr/solr-9.3.0/server/solr/collection1/conf/schema.xml

echo "Atualizando o SOLR"
curl "http://localhost:8983/solr/admin/cores?action=RELOAD&core=collection1"
echo "End"


service solr restart
./restart