"""
Your module description
Autor: Bocar BA
Email: babocarba96@gmail.com
"""



import re

fichier1= open("preproinsulin-seq.txt",'r')
file=fichier1.read()

#Affection des contenu du fichier à une variable de type chaine
contenu = file

#Suppression des chaines suivant : [ORIGIN, //, 1, 61] et les espaces et retour à la ligne
contenu = re.sub("ORIGIN|//|[0-9]+|\n| ","",contenu)
print(contenu)

#Apres extraction des caracteres on ajoute le contenu dans un new fichier 
fichier2 = open("preproinsulin_seq_clean.txt.",'w')
fichier2.write(contenu)

#Extraction des 24 premiers caracteres du fichier 2
var_1_24=contenu[0:24]
fichier3 = open("lsinsulin-seq-clean.txt",'w')
fichier3.write(var_1_24)
print(len(var_1_24))

#Extraction de 25 à 54 du fichier 2
var_25_54=contenu[24:54]
fichier4 = open("binsulin-seq-clean.txt",'w')
fichier4.write(var_25_54)
print(len(var_25_54))

#Extraction de 55 à 89 du fichier 2
var_55_89=contenu[54:89]
fichier5 = open("cinsulin-seq-clean.txt",'w')
fichier5.write(var_55_89)
print(len(var_55_89))

#Extraction de 90 à 110 du fichier 2
var_90_110 =contenu[89:110]
fichier6 = open("ainsulin-seq-clean.txt",'w')
fichier6.write(var_90_110)
print(len(var_90_110))

#fermuture des fichiers
fichier1.close
fichier2.close
fichier3.close
fichier4.close
fichier5.close
fichier6.close