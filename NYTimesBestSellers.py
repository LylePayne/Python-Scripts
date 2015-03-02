import requests

##Will have to enter API key in the URL instead of YOUR_KEY to work
response = requests.get("http://api.nytimes.com/svc/books/v3/lists/date/hardcover-fiction/response_format.json?.optional-param1=value1&api-key=YOUR_KEY")

##Returns a list of bestsellers from the week and list selected within the URL above.
##Date when not specified returns the most recent list
##"hardcover-fiction" can be swaped out for other Best Seller lists
for i, book in enumerate(response.json()["results"]["books"]):
    print i+1, book["title"]
    print '\t', "Author: ", book["author"]
    print '\t', "Weeks on List: ", book["weeks_on_list"]
    print