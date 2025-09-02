export ID=3
export API_TOKEN="your_api_token_here"
curl -X DELETE -H "X-Dataverse-key:$API_TOKEN" "$SERVER_URL/api/licenses/$ID"