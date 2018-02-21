
from bs4 import BeautifulSoup

from os import listdir




	


def filter( arch ):


	with open("/home/anonymous/Desktop/coleccionESuja2018/" + arch) as ls:

		soup = BeautifulSoup(ls, "html.parser")

	
	#Get Title
	text = soup.title.text


	#Get Date
	date = soup.find("div", attrs = {"class" : "field-item odd"})
	text = text + " " + date.find("span").text

	#Get Body
	body = soup.find_all("p")
	for bd in body:
		text = text + " " + bd.text

	
	#Get Tags
	topics = soup.find_all("a", attrs = {"rel" : "tag"})
	for i in topics:
		text = text + " " + i.text

	#Get Rute
	rute = soup.find("div", attrs = {"class" : "breadcrumb"})
	for rt in rute.find_all("a"):
		 text = text + " " + rt.text 
		

	#Get Author
	author = soup.find("div", attrs = {"class" : "submitted"})
	user = author.text.split()
	text = text + " " + user[2]
	
	ls.close()

	return text
	






for arch in listdir("/home/anonymous/Desktop/coleccionESuja2018/"):

	print "!!!!!!!!!!!!!!!!!!!!!!!!" + arch + "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"

	print filter( arch )


print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
