import random
import requests
from bs4 import BeautifulSoup

requestAdress = requests.get("https://www.imdb.com/chart/top")
soup = BeautifulSoup(requestAdress.content, "html.parser")

films = soup.find_all("td", attrs = {"class":"titleColumn"})
rates = soup.find_all("td", attrs = {"class":"ratingColumn"})

random = random.randint(0,99)

print("We suggest you to watch: " + films[random].a.text + " " + films[random].span.text + '\033[0;32m'
+ " (rate:" + rates[random*2].strong.text + ")" + '\033[0m')

director = films[random].a.get("title")
print("Director is " + '\033[0;35m' + director[: director.index('(dir.)')] + '\033[0m' + "\n" )

choice = input("Do you want to see IMDB Top 100 list? (Y/N): ")

if(choice == 'Y' or choice == 'y'):
	index = 0
	rateIndex = 0
	while (index < 100):
		#print(films[i].a.text, "(IMDB rate: " + rates[rateIndex].strong.text + ")")
		#print((index+1),")",'{:75}'.format(films[index].a.text), '{:>10}'.format("(rate:"+rates[rateIndex].strong.text+")"))
		print( (str)(index+1) + ") "  + films[index].a.text + " " + films[index].span.text )

		print('\033[0;32m' + "IMDB Rate: " + rates[rateIndex].strong.text + '\033[0m')

		director = films[index].a.get("title")
		print( "Director: " + director[: director.index('(dir.)')] )

		print("-----------------------------------")
		index = index + 1
		rateIndex = rateIndex + 2

