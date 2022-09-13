import requests
from bs4 import BeautifulSoup as bs

github_profile = "http://github.com/haraGADygyl"
request = requests.get(github_profile)

scraper = bs(request.content, "html.parser")
profile_picture = scraper.find("img", {"alt": "Avatar"})["src"]
print(profile_picture)
