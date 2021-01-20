# Programme intéractif a la console
# Pour Dimanche 06 Décembre 2020
#Nom:         Un quiz (Un quiz jeu.py)
#But:         quiz
#Auteur:      Alioune Badara Seck
#Crée:        03-DEC-2020
#Mis à jour:  06-DEC-2020
nom = input('Quel est votre nom:')
print('Bienvenue,'+ nom + '!')
print("Vous venez d'entrer dans un petit quiz avec Alioune")
print()
print("Commençons")
print("(PS: toute les réponses commencent avec une majuscule)")
print("")
Un = input("Quel est le Symbole de L'Hélium: ")
Deux = input("Quel est la capitale du Canada: ")
Trois = input("Quel est le nom de famille du prof d'info: ")
Un1 = "He"
Deux2 = "Ottawa"
Trois3 = "Crowley"
if Un==Un1:
  print("1.correct")
else:
  print("1.Incorrect")
if Deux==Deux2:
  print("2.correct")
else:
  print("2.Incorrect")
if Trois==Trois3:
  print("3.correct")
else:
  print("3.Incorrect")
print("")
print("Merci"+" "+ nom +" "+ "pour votre temps.")
Merci = input()

