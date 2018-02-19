
from bs4 import BeautifulSoup


with open("/home/anonymous/Desktop/coleccionESuja2018/es_26142.html") as ls:

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
rute = soup.find("div", attrs = {"class" : "breadcrumb"})

rute.find_all("a")

#for i in rute:
	#print i.string

inta = 0
#Get Author
author = soup.find("div", attrs = {"class" : "submitted"})
user = author.string.split()

print user[2]


print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
