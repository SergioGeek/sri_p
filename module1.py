from bs4 import BeautifulSoup

import os

from os import listdir

import re

import unicodedata

from time import time

import configparser

from nltk.corpus import stopwords



	


def filter( arch ): # Esta función recopila lo necesario de la noticia


	html_file = open("/home/anonymous/Desktop/coleccionESuja2018/" + arch, "r")

	soup = BeautifulSoup(html_file, "lxml")

	
	# Get Title
	text = soup.title.text


	# Get Date
	date = soup.find("div", attrs = {"class" : "field-item odd"})
	text = text + " " + date.find("span").text

	#Get Body
	body = soup.find_all("p")
	for bd in body:
		text = text + " " + bd.text

	
	# Get Tags
	topics = soup.find_all("a", attrs = {"rel" : "tag"})
	for i in topics:
		text = text + " " + i.text

	# Get Rute
	rute = soup.find("div", attrs = {"class" : "breadcrumb"})
	for rt in rute.find_all("a"):
		 text = text + " " + rt.text 
		

	# Get Author
	author = soup.find("div", attrs = {"class" : "submitted"})
	user = author.text.split()
	text = text + " " + user[2]
	
	html_file.close()

	return text
	


def clean( filtered ): # Esta función limpia el string dado

	cleaned = filtered.lower() # Pone a minúscula
	
	pattern = re.compile(r'\W+') # Separa por síbolos no alfanuméricos
	
	fich_fin = pattern.split(elimina_tildes(cleaned)) # Elimina tildes y tokeniza

	cleaned = []

	for archw in fich_fin : 
		cleaned.append(archw)

	return cleaned
	

def stopper( cleaned ):

	stopper_fich = []

	stopWords = set(stopwords.words('spanish'))

	for c in cleaned:
		if c not in stopWords:
			stopper_fich.append(c)

	return stopper_fich
	

def elimina_tildes(s):
   return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))
 



tini = time()

tt = 0
 

#######################################################################-Main-##########################################################################

# Lectura de archivo de configuración
confg_file = configparser.ConfigParser()
confg_file.read("config.cfg")


# Creación de directorio destino (cleaned)
if "coleccionESuja2018cleaned" not in listdir(confg_file["PATHS"]["WritingPath"]): # Si ya está, el directorio no se crea
	os.mkdir(confg_file["PATHS"]["WritingPath"] + "coleccionESuja2018cleaned")

# Creación de directorio destino (stopper)
if "coleccionESuja2018stopper" not in listdir(confg_file["PATHS"]["WritingPath"]): # Si ya está, el directorio no se crea
	os.mkdir(confg_file["PATHS"]["WritingPath"] + "coleccionESuja2018stopper")




for arch in listdir(confg_file["PATHS"]["ReadingPath"]):

	arch_cleaned = confg_file["PATHS"]["WritingPath"] + "coleccionESuja2018cleaned/" + arch[0:8] + ".txt"

	arch_stopper = confg_file["PATHS"]["WritingPath"] + "coleccionESuja2018stopper/" + arch[0:8] + ".txt"

	cleaned = clean(filter(arch))

	fc = ""

	for c in cleaned:
		fc += (c + '\n')

	fich_cleaned = open(arch_cleaned, 'w')

	fich_cleaned.write(fc)
		
	fich_cleaned.close()

	sl = ""

	stopper_list = stopper(cleaned)

	for slw in stopper_list:
		sl += (slw + '\n')

	fich_stopper = open(arch_stopper, 'w')	

	fich_stopper.write(sl)

	fich_stopper.close()

	

tfin = time()

tt = tfin - tini



print ("Tiempo de ejecucion: " + str(tt))

