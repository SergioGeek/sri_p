
from bs4 import BeautifulSoup

from os import listdir




	


def filter( arch ):

	with open("/home/anonymous/Desktop/coleccionESuja2018/" + arch) as ls:

		soup = BeautifulSoup(ls, "html.parser")



	

	#Get Title
	print soup.title.string


	#Get Date
	date = soup.find("div", attrs = {"class" : "field-item odd"})
	print date.find("span").string

	#Get Body
	body = soup.find_all("p")
	print body[1].string

	#Get Tags
	topics = soup.find_all("a", attrs = {"rel" : "tag"})

	for i in topics:
		print i.string

	#Get Rute
	rute = soup.find("div", attrs = {"class" : "terms terms-inline"})

	if rute:
		print rute.find("a").string
	else:
		print "home"
		

	#Get Author
	author = soup.find("div", attrs = {"class" : "submitted"})
	user = author.string.split()

	print user[2]

	ls.close()
	






for arch in listdir("/home/anonymous/Desktop/coleccionESuja2018/"):

	print "!!!!!!!!!!!!!!!!!!!!!!!!" + arch + "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"

	filter( arch )


print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
