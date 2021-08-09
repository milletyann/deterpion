# -*- coding: utf-8 -*-

import numpy as np
from tkinter import *
from random import randint

def modif(mat,i,j,val):
	assert val in [0, 1]
	mat[i][j] = val

def det_calc(mat):
	# renvoie si on peut calculer le determinant ou pas
	try:
		det = np.linalg.det(mat)
		return True
	except:
		return False

def det(mat):
	return np.linalg.det(mat)

def tirage():
	return randint(0, 1)

### feature freeze v.1
	
### v.2

def remplir(mat):
	# remplir le frame tkinter à partir de la matrice actuelle
	n = len(mat)
	for i in range(n):
		for j in range(n):
			if mat[i][j] == '?':
				txt = canvas.create_text(i*90 +45, j*90 +45, text="?", font="Arial 16 italic", fill="blue")
				canvas.pack()
			elif mat[i][j] == 1:
				txt = canvas.create_text(i*90 +45, j*90 + 45, text="1", font="Arial 16 italic", fill="blue")
				canvas.pack()
			else:
				txt = canvas.create_text(i*90 +45, j*90 + 45, text="0", font="Arial 16 italic", fill="blue")
				canvas.pack()


### not v.n  n>2

def nb_indet(mat):
	c, n = 0, len(mat)
	for i in range(n):
		for j in range(n):
			if mat[i][j] == '?':
				c +=1
	return c

def transposee(mat):
	n = len(mat)
	return [[mat[j][i] for j in range(n)] for i in range(n)]

def recherche_coli(mat):
	# renvoie le booléen 'il existe 2 lignes égales'
	n = len(mat)
	for i in range(n):
		for k in range(i +1, n):
			if mat[i] == mat[k]:
				return True
	return False
