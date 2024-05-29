#:ControlledVocabularyCustomJavaScript allows a JavaScript file to be loaded into the dataset page
#for the purpose of showing controlled vocabulary as a list (with optionally translated values) such as author names.

#To specify the URL for a custom script covoc.js to be loaded from an external site:

curl -X PUT -d 'https://example.com/js/covoc.js' http://localhost:8080/api/admin/settings/:ControlledVocabularyCustomJavaScript

#To remove the custom script URL:

curl -X DELETE http://localhost:8080/api/admin/settings/:ControlledVocabularyCustomJavaScript

#Please note that :CVocConf is a better option if the list is large or needs to be searchable from an external service using protocols such as SKOSMOS.