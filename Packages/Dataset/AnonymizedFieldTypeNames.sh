#A comma-separated list of field type names that should be ‘withheld’ when dataset access occurs via a
#Private Url with Anonymized Access (e.g. to support anonymized review).
#A suggested minimum includes author, datasetContact, and contributor, but additional fields such as depositor,
#grantNumber, and publication might also need to be included.

curl -X PUT -d 'author, datasetContact, contributor, depositor, grantNumber, publication' http://localhost:8080/api/admin/settings/:AnonymizedFieldTypeNames