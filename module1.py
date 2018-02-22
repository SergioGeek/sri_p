
from bs4 import BeautifulSoup

import os

from os import listdir

import re

import unicodedata

from time import time



	


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
	


def clean( filtered ):

	cleaned = filtered.lower()
	
	pattern = re.compile(r'\W+')

	return pattern.split(elimina_tildes(cleaned))




def elimina_tildes(s):
   return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))
 

tini = time()

tf = 0

os.mkdir("/home/anonymous/Desktop/coleccionESuja2018res")

for arch in listdir("/home/anonymous/Desktop/coleccionESuja2018/"):



	newarch = "/home/anonymous/Desktop/coleccionESuja2018res/" + arch[0:8] + ".txt"
	
	fich = open(newarch, 'w')

	forini = time()

	for archw in clean( filter( arch )):
		fich.write(archw + '\n')

	forend = time()
	
	tf += (forend - forini)

	fich.close()

tfin = time()

te = tfin - tini



print "Tiempo de ejecucion: " + str(te)

print "Tiempo de for: " + str(tf)

