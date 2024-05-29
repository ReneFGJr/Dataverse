#Se :SolrFullTextIndexing está setado como verdadeiro,
# o conteúde dos arquivos de qualquer tamanho será indexado
# Para definir um limite embytes utilize o parametro:

curl -X PUT -d 314572800 http://localhost:8080/api/admin/settings/:SolrMaxFileSizeForFullTextIndexing