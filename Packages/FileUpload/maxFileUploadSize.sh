#Ex: 2Giga = 2*1024*1024*2014
#              (k)  (m)  (g)
curl -X PUT -d 2147483648 http://localhost:8080/api/admin/settings/:MaxFileUploadSizeInBytes