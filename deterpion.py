# -*- coding: utf-8 -*-

import numpy as np
from fonctions import *
from random import randint


print('Deterpion dans Z/2Z')
n = int(input('Quelle dimension? (Les champions prennent n>17) '))

# creation de la matrice
mat = []
for j in range(n):
	ligne = []
	for i in range(n):
		ligne.append('?')
	mat.append(ligne)


print("Celui qui défend doit empêcher la matrice d'être inversible.")
defenseur = input('Nom du défenseur: ')
attaquant = input("Nom de l'attaquant: ")

P = [[defenseur, 'le défenseur'], [attaquant, "l'attaquant"]]
p = tirage()
# i.e. si p == 0 c'est le defenseur qui commence
print('{} ({})commence'.format(P[p][0], P[p][1]))
print('La matrice de départ est: \n {} \n -------------------------------- \n'.format(np.array(mat)))

tdb = p
while not(det_calc(mat)):
	if tdb%2 == 1:
		print('{} à toi!\n'.format(attaquant))
	else:
		print("{} c'est ton tour\n".format(defenseur))
	val = int(input('0 ou 1? '))
	i = int(input('Choisis ta ligne (i): '))
	j = int(input('Choisis ta colonne (j): '))
	print('\n')
	c = 0
	while mat[i][j] != '?':
		if c == 0:
			print("{}, tu as choisi une case déjà prise. Essaie encore >>>".format(P[tdb%2][0]))
		elif c == 1:
			print('Mais tu le fais exprès? Tu as encore choisi une case occupée, réfléchis un peu!')
		elif c == 2:
			print("Mais quel idiot regarde avant de dire n'importe quoi...")
		else:
			print('Toujours pas... (Tu es un mongole à la puissance {})'.format(c+1))
		val = int(input('0 ou 1? '))
		i = int(input('Choisis ta ligne (i): '))
		j = int(input('Choisis ta colonne (j): '))
		c += 1
	modif(mat, i, j, val)
	print('matrice actuelle: \n {} \n --------------------------------'.format(np.array(mat)))
	tdb += 1

if det(mat)%2 == 0:
	print("La matrice n'est pas inversible dans Z/2Z, {} gagne.".format(P[0][0]))
else:
	print("La matrice est inversible, l'attaquant l'emporte.".format(P[1][0]))
input()
