import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.imdb.com/chart/top")
soup = BeautifulSoup(r.content, "html.parser")

films = soup.find_all("td", attrs = {"class":"titleColumn"})
rates = soup.find_all("td", attrs = {"class":"ratingColumn"})

i = 0
rateIndex = 0
while (i <= 100):
	print(films[i].a.text, "(IMDB rate: " + rates[rateIndex].strong.text + ")")
	i = i + 1
	rateIndex = rateIndex + 2
