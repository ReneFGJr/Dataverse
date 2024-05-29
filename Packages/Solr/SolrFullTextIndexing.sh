#Indexar ou não o conteúdo de arquivos como PDFs.
#O padrão é falso.

curl -X PUT -d true http://localhost:8080/api/admin/settings/:SolrFullTextIndexing