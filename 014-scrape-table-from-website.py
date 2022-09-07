import urllib.request
import pandas as pd

url = "https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites"

with urllib.request.urlopen(url) as u:
    html = u.read()

data = pd.read_html(html)[0]
data.to_csv("programming.csv")
print(data)
