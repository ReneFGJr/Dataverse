# Desabilitar acesso do RDATA

 curl -X PUT -d "{\"default\": 104857600, \"Rdata\": 1}" "http://localhost:8080/api/admin/settings/:TabularIngestSizeLimit"