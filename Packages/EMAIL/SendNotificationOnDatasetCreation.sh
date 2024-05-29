#A boolean setting that, if true, will send an email and notification to users when a Dataset is created.
#Messages go to those, other than the dataset creator, who have the ability/permission necessary to publish the dataset.
#The intent of this functionality is to simplify tracking activity and planning to follow-up contact.

curl -X PUT -d true http://localhost:8080/api/admin/settings/:SendNotificationOnDatasetCreation