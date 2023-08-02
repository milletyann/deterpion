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
    
# partie calcul de déterminant sur matrice partielle


