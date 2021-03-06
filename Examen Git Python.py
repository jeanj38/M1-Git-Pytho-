# -*- coding: utf-8 -*-
"""Copie de Untitled12.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1onhlWtmM48jjynYvRMpe_UW4QLfzwPSI

# Implémentation de la fonction polynomiale
"""

import math 
 
def polynome(x): # Création de la fonction polynamiale 
  
  if (type(x) == str) : # Vérifie que l'utilisateur que l'utilisateur saisi une chaine de caractère
    print("Les chaines de caractère ne sont pas pris en compte")
    print("Veuillez saisir un entier pour x") # dis à l'utilisateur de saisir une nouvelle valeur pour x
    x = int(input()) # saisi de la valeur de x

  elif (x < 0) : # Vérifie que l'utilisateur que l'utilisateur saisi une chaine de caractère
    print("Les entiers négatifs ne sont pas pris en compte")
    print("Veuillez saisir un entier pour x") # dis à l'utilisateur de saisir une nouvelle valeur pour x
    x = int(input()) # saisi de la valeur de x
  
  elif (type(x) == complex) : # Vérifie que l'utilisateur que l'utilisateur saisi une chaine de caractère
    print("Les nombres complexes ne sont pas pris en compte")
    print("Veuillez saisir un entier pour x") # dis à l'utilisateur de saisir une nouvelle valeur pour x
    x = int(input()) # saisi de la valeur de x
  
  elif (len(str(x)) > 10) : 
    print("L'entier saisi est trop grand")
    print("Veuillez saisir un entier inférieur à 10 caractères") # dis à l'utilisateur de saisir un entier plus petit 
    x = int(input()) # saisi de la valeur de x

  elif (x < 0.01) : 
    print("L'entier saisi est trop petit")
    print("Veuillez saisir un entier supérieur a 0.01") # dis à l'utilisateur de saisir un entier plus petit 
    x = int(input()) # saisi de la valeur de x
  
  y = x**3 - (1.5)*x**2 - 6*x + 5 # Calcul la fonction polynomiale x^3 - 1.5x^2 - 6x +5
  
  return y # retourne y

polynome(0.005)

"""Implémentation de la fonction factorielle 

"""

def factorial(n): # Création de la fonciton factorielle
  if (len(str(n)) > 7): # Vérifie que n est une chaine de caractère
    print("L'entier saisi est trop grand")
    print("Veuillez saisir un entier positif inférieur a 7 caractères")
    n = int(input()) # saisi de la valeur de x
  
  elif (n < 0):  # vérifie que n est un négatif 
    print("Les entiers négatifs ne sont pas en pris en compte")
    print("veuillez saisir un entier positif")
    n = int(input()) # saisi de la valeur de x   
    
  elif (type(n) == str):  # vérifie que n est une chaine de caractère 
    print("Les chaines de caractère ne sont pas pris en compte")
    print("veuillez saisir un entier positif")
    n = int(input()) # saisi de la valeur de x 
    
  elif (type(n) == complex): # vérifie que n est un complexe
    print("Les nombres complexes ne sont pas pris en compte")
    print("veuillez saisir un entier positif")
    n = int(input()) # saisi de la valeur de x
    
  elif (n == float) : # Vérifie que n est un flottant
    print("Les nombres à virgules ne sont pas pris en compte")
    print("Veuillez saisir un entier supérieur à 0")
    x = int(input()) # saisi de la valeur de x
  
  
  if n == 0: 
    return 1 # retourne 1 lorque n = 0
    
  else: 
    
    fact = 1
    while(n > 1): # vérifie que la valaur saisie est différente de 1
      fact *= n 
      n -= 1
    return fact # renvoie le factorielle de n

factorial(5)

"""Implémentation de la suite de fibonacci"""

nterms = int(input("Entrez un nombre: "))
 
n1 = 0
n2 = 1
 
print("\n la suite fibonacci est :")
print(n1, ",", n2, end=", ")
 
for i in range(2, nterms):
  suivant = n1 + n2
  print(suivant, end=", ")
 
  n1 = n2
  n2 = suivant

