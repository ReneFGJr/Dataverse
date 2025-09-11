import dataverse_create
import dataset_create

if __name__ == "__main__":

    #dataverse_create.create_dataverse(
    #    dataverse_alias="repatriacao_confoa",
    #    name="Teste Repatriação CONFOA",
    #    affiliation="UFRGS",
    #    description="Dataverse de teste para o Repatriação de datasets"
    #)

    dataset_create.create_dataset(
        dataverse_alias="repatriacao_confoa",
        json_file="dataset4.json"
    )