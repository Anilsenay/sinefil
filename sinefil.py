import random
import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.imdb.com/chart/top")
soup = BeautifulSoup(r.content, "html.parser")

films = soup.find_all("td", attrs = {"class":"titleColumn"})
rates = soup.find_all("td", attrs = {"class":"ratingColumn"})

random = random.randint(0,99)
print("We suggest you to watch: " + films[random].a.text + " (rate:" + rates[random*2].strong.text + ")")
choice = input("Do you want to see IMDB Top 100 list? (Y/N): ")

if(choice == 'Y' or choice == 'y'):
	i = 0
	rateIndex = 0
	while (i < 100):
		#print(films[i].a.text, "(IMDB rate: " + rates[rateIndex].strong.text + ")")
		print((i+1),")",'{:71}'.format(films[i].a.text), '{:>10}'.format("(rate:"+rates[rateIndex].strong.text+")"))
		i = i + 1
		rateIndex = rateIndex + 2

