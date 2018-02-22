
from bs4 import BeautifulSoup

import os

from os import listdir

import re

import unicodedata

from time import time



	


def filter( arch ):

	

	html_file =  open("/home/anonymous/Desktop/coleccionESuja2018/" + arch, "r")
	
	opningi = time()
	soup = BeautifulSoup(html_file.read(), "lxml")
	opningf = time()
	opning = opningf - opningi

	
	#Get Title
	text = soup.title.text

	
	#Get Date
	date = soup.find("div", attrs = {"class" : "field-item odd"})
	text = text + " " + date.find("span").text

	

	for1i = time()
	#Get Body
	body = soup.find_all("p")
	for bd in body:
		text = text + " " + bd.text
	for1f = time()
	for1 = for1f - for1i

	for2i = time() 
	#Get Tags
	topics = soup.find_all("a", attrs = {"rel" : "tag"})
	for i in topics:
		text = text + " " + i.text
	for2f = time()
	for2 = for2f - for2i

	for3i = time()
	#Get Rute
	rute = soup.find("div", attrs = {"class" : "breadcrumb"})
	for rt in rute.find_all("a"):
		 text = text + " " + rt.text 
	for3f = time()
	for3 = for3f - for3i
		
	sp1i = time()
	#Get Author
	author = soup.find("div", attrs = {"class" : "submitted"})
	user = author.text.split()
	text = text + " " + user[2]
	sp1f = time()
	sp1 = sp1f - sp1i
	
	html_file.close()

	return text, for1, for2, for3, sp1, opning
	


def clean( filtered ):

	cleaned = filtered.lower()
	
	pattern = re.compile(r'\W+')

	return pattern.split(elimina_tildes(cleaned))




def elimina_tildes(s):
   return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))
 

carcht = 0

oflt = 0

filtt = 0

clt = 0

closet = 0

wrt = 0

te = 0

for1 = 0

for2 = 0

for3 = 0

sp1 = 0

opning = 0

for1s = 0

for2s = 0

for3s = 0

sp1s = 0

opnings = 0

tini = time()



os.mkdir("/home/anonymous/Desktop/coleccionESuja2018res")

for arch in listdir("/home/anonymous/Desktop/coleccionESuja2018/"):

	carchi = time()
	newarch = "/home/anonymous/Desktop/coleccionESuja2018res/" + arch[0:8] + ".txt"
	carchf = time()
	carcht += (carchf - carchi)
	
	ofli = time()
	fich = open(newarch, 'w')
	oflf = time()
	oflt += (oflf - ofli)
	
	fili = time()
	filt, for1, for2, for3, sp1, opning = filter( arch )
	
	for1s += for1
	for2s += for2
	for3s += for3
	sp1s += sp1
	opnings += opning

	filf = time()
	filtt += (filf - fili)

	cli = time()
	clnd = clean( filt )
	clf = time()
	clt += (clf - cli)

	wri = time ()
	for archw in clnd :
		fich.write(archw + '\n')
	wrf = time()
	wrt += (wrf - wri)

	closei = time()
	fich.close()
	closef = time()
	closet += (closef - closei)


tfin = time()

te = tfin - tini





print "Tiempo de ejecucion: " + str(te)
print "Tiempo creando archivos: " + str(carcht)
print "Tiempo abriendo archivo: " + str(oflt)
print "Tiempo filtrando: " + str(filtt)
print "Tiempo limpiando: " + str(clt)
print "Tiempo volcando: " + str(wrt)

print "Tiempo f1: " + str(for1s)
print "Tiempo f2: " + str(for2s)
print "Tiempo f3: " + str(for3s)
print "Tiempo sp: " + str(sp1s)
print "Tiempo opening: " + str(opnings)


