import csv
from urllib.request import urlopen
import pandas as pd

from bs4 import BeautifulSoup

html = urlopen("https://en.wikipedia.org/wiki/Comparison_of_programming_languages")
soup = BeautifulSoup(html, "html.parser")
table = soup.findAll("table", {"class": "wikitable"})[0]
rows = table.findAll("tr")

with open("../resources/languages.csv", "wt+", encoding="utf-8") as f:
    writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in rows:
        row = []
        for cell in i.findAll(["td", "th"]):
            row.append(cell.get_text().strip())
        writer.writerow(row)

a = pd.read_csv("../resources/languages.csv")
a.head()
