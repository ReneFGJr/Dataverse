export API_TOKEN=SEU_TOKEN
export ID=ID_DA_LICENCA
curl -X PUT -H "Content-Type: application/json" -H "X-Dataverse-key:$API_TOKEN" "$SERVER_URL/api/licenses/$ID/:active/false"
