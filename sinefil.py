import random
import requests
from bs4 import BeautifulSoup

print("Welcome to Sinefil !\n")
print("1- Random suggestion by top rated films \n"	+
	"2- IMDB Top 100 List \n" +
	"3- Top lists by genre \n" +
	"4- My random suggestion \n" +
	"5- My suggestion list \n" +
	"6- Find a film's rates by platforms \n" +
	"q- For quit")

choice = input("Write your choice: ")
print("")

############################ 1- Random suggestion ###################################
if(choice == "1"):

	requestAdress = requests.get("https://www.imdb.com/chart/top")
	soup = BeautifulSoup(requestAdress.content, "html.parser")
	
	films = soup.find_all("td", attrs = {"class":"titleColumn"})
	rates = soup.find_all("td", attrs = {"class":"ratingColumn"})
	
	random = random.randint(0,99)

	print("We suggest you to watch: " + films[random].a.text + " " + films[random].span.text + '\033[0;32m'
		+ " (rate:" + rates[random*2].strong.text + ")" + '\033[0m')

	director = films[random].a.get("title")
	print("Director is " + '\033[0;35m' + director[: director.index('(dir.)')] + '\033[0m' + "\n" )

######################### 2- Top 100 ###############################################
elif(choice == "2"):
    requestAdress = requests.get("https://www.imdb.com/chart/top")
    soup = BeautifulSoup(requestAdress.content, "html.parser")
    
    films = soup.find_all("td", attrs = {"class":"titleColumn"})
    rates = soup.find_all("td", attrs = {"class":"ratingColumn"})

    index = 0
    rateIndex = 0
    while (index < 100):

        print( (str)(index+1) + ") "  + films[index].a.text + " " + films[index].span.text )
        print('\033[0;32m' + "IMDB Rate: " + rates[rateIndex].strong.text + '\033[0m')

        director = films[index].a.get("title")
        print( "Director: " + director[: director.index('(dir.)')] )

        print("-----------------------------------")
        index = index + 1
        rateIndex = rateIndex + 2

######################### 3- Top list by genre ##########################################
elif(choice == "3"):
	print("Genres: \n" +
    "Action \n" +
    "Adventure \n" +
    "Animation \n" +
    "Biography \n" +
    "Comedy \n" +
    "Crime \n" +
    "Drama \n" +
    "Family \n" +
    "Fantasy \n" +
    "Film-Noir \n" +
    "History \n" +
    "Horror \n" +
    "Music \n" +
    "Musical \n" +
    "Mystery \n" +
    "Romance \n" +
    "Sci-Fi \n" +
    "Sport \n" +
    "Thriller \n" +
    "War \n" +
    "Western \n" )
	genre = input("Write your choice: ")
	print("")

	requestAdress = requests.get("https://www.imdb.com/search/title?genres="+ genre +"&sort=user_rating,desc&title_type=feature&num_votes=25000,&view=simple")
	soup = BeautifulSoup(requestAdress.content, "html.parser")

	films = soup.find_all("div", attrs = {"class":"col-title"})
	rates = soup.find_all("div", attrs = {"class":"col-imdb-rating"})
	#directors = soup.find_all("p", attrs = {"class":""})

	index = 0
	rateIndex = 0
	while (index < 50):
		year = films[index].span.text
		print( (str)(index+1) + ") "  + films[index].a.text + " " + year[year.index('('): year.index(')')+1] )
		print('\033[0;32m' + "IMDB Rate: " + rates[rateIndex].strong.text.replace(' ', "").replace('\n', "") + '\033[0m')

		text = (str)(films[index].span)
		director = text[text.find('title="') + 7 : text.find('(dir.)')]
		print("Director: " + director)

		print("-----------------------------------")
		index = index + 1
		rateIndex = rateIndex + 1

##################################### 4- My random suggestion ######################################
elif(choice == "4"):
	requestAdress = requests.get("https://letterboxd.com/anilsenay/list/onerilir/")
	soup = BeautifulSoup(requestAdress.content, "html.parser")

	films = soup.find_all("img", attrs = {"class":"image"})

	random = random.randint(0, len(films))
	print("A random suggestion from movies I watched this year is " + '\033[0;32m' + films[random].get("alt").upper() + '\033[0m')
	print("")

#################################### 5- My list #####################################################
elif(choice == "5"):
	requestAdress = requests.get("https://letterboxd.com/anilsenay/list/onerilir/")
	soup = BeautifulSoup(requestAdress.content, "html.parser")

	films = soup.find_all("img", attrs = {"class":"image"})
	print("______________________________________\n")	
	print("SUGGESTED MOVIES I WATCHED IN 2019")
	print("______________________________________\n")
	index = 0
	while(index < len(films)):
		print( (str)(index+1) + ") " + films[index].get("alt"))
		index = index + 1
	print("\nYou can check my letterbox account for more: " + '\033[0;32m' + "https://letterboxd.com/anilsenay" + '\033[0m')

#################################### 6- Find rate from platforms ####################################
elif(choice == "6"):
	movieName = input("Which movie do you want to search: ")
	
	## IMDB ##
#	requestAdressIMDB = requests.get("https://www.imdb.com/search/title?title="+movieName+"&view=simple")
#	soup = BeautifulSoup(requestAdressIMDB.content, "html.parser")
#	
#	films = soup.find_all("div", attrs = {"class":"col-title"})
#	imdbRates = soup.find_all("div", attrs = {"class":"col-imdb-rating"})
#
#	print(films[0].span.text.replace('\n', "") + " IMDB rate: " + imdbRates[0].strong.text.replace(' ', "").replace('\n', "") )

	    ## IMDB AND METACRITIC ##
	requestAdressIMDB = requests.get("https://www.imdb.com/search/title?title="+movieName+"&view=advanced")
	soup = BeautifulSoup(requestAdressIMDB.content, "html.parser")
    
	films = soup.find_all("h3", attrs = {"class":"lister-item-header"})
	imdbRates = soup.find_all("div", attrs = {"class":"ratings-bar"})
	metacriticRate = soup.find_all("span", attrs = {"class":"metascore favorable"})
	informations = soup.find_all("p", attrs = {"class":"text-muted"})
	stars = soup.find_all("div", attrs = {"class":"lister-item-content"})
	print("________________________________________________\n")
	print(films[0].text.replace('\n', ""))
	print("")
	print(informations[0].text.replace('\n', " ")[1:])
	print(stars[0].text[stars[0].text.find("Director"): stars[0].text.find("Votes")].replace("\n", '').replace("     ","\n").replace('|', "") )
	print("________________________________________________")
	print("\nIMDB rate: " + imdbRates[0].strong.text.replace(' ', "").replace('\n', "") )
	print("Metacritic rate: " +  metacriticRate[0].text)

else:
	print("Wrong input")
