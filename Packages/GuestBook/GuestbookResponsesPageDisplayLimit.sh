#Limit on how many guestbook entries to display on the guestbook-responses page.
#By default, only the 5000 most recent entries will be shown. Use the standard settings API in order
#to change the limit. For example, to set it to 10,000, make the following API call:

curl -X PUT -d 10000 http://localhost:8080/api/admin/settings/:GuestbookResponsesPageDisplayLimit