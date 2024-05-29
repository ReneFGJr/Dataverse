#A JSON-structured setting that configures Dataverse to associate specific metadatablock fields with external vocabulary services and specific vocabularies/sub-vocabularies managed by that service. More information about this capability is available at Metadata Customization.

#Scripts that implement this association for specific service protocols are maintained at https://github.com/gdcc/dataverse-external-vocab-support. That repository also includes a json-schema for validating the structure required by this setting along with an example metadatablock and sample :CVocConf setting values associating entries in the example block with ORCID and SKOSMOS based services.

wget https://gdcc.github.io/dataverse-external-vocab-support/examples/config/cvoc-conf.json

curl -X PUT --upload-file cvoc-conf.json http://localhost:8080/api/admin/settings/:CVocConf