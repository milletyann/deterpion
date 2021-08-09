# -*- coding: utf-8 -*-

from tkinter import *
from tkinter.messagebox import *
import fonctions
from random import randint

fenetre = Tk()
fenetre.title('Deterpion by Gryson')
fenetre.geometry('800x550')
fenetre.resizable(width=True, height=True)

# une sorte de titre
label = Label(fenetre, text='Deterpion').pack(side=TOP, padx= 10, pady=10)


# un petit menu pour plus tard
message = "Ce jeu a été inventé au début des années 2000 par un groupe d'étudiants de l'ENS parmi lequel figurait Alexis Gryson, professeur de mathématiques au lycée Jean-Baptiste Kléber de Strasbourg."

def callback():
    showinfo('Le saviez-vous?', message)

def nothing_for_now():
	pass

def set_val_nv_pion():
	pass

menubar = Menu(fenetre)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Nouvelle partie", command=nothing_for_now)
menu1.add_separator()
menu1.add_command(label="Arrêter Partie", command=fenetre.quit)
menubar.add_cascade(label="Partie", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Statistiques", command=nothing_for_now)
menu2.add_command(label="Rien lol", command=nothing_for_now)
menubar.add_cascade(label="Session", menu=menu2)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="About", command=callback)
menubar.add_cascade(label="Help", menu=menu3)

fenetre.config(menu=menubar)


# les differentes parties de l'ecran

Frame1 = LabelFrame(fenetre, text='Le champ de bataille')
Frame1.pack(side=LEFT, fill= 'both', expand='yes', padx=30, pady=30)

Frame2 = LabelFrame(fenetre, text='Paramètres partie', borderwidth=2, relief=GROOVE)
Frame2.pack(side=RIGHT, expand='yes', padx=30, pady=100)


# la ou on balance la matrice
def faire_mat(n):
	taille= 380/n
	canvas = Canvas(Frame1, width=n*taille, height=n*taille, background='beige')
	for i in range(n+1):
		ligne = canvas.create_line(i*taille, 0, i*taille, n*taille)
		canvas.pack()
	for i in range(n+1):
		ligne = canvas.create_line(0, i*taille, n*taille, i*taille)
		canvas.pack()

	mat_alea = [['?' for k in range(n)] for i in range(n)]
	for i in range(n):
		for j in range(n):
			if mat_alea[i][j] == '?':
				canvas.create_text(i*taille +(taille/2), j*taille +(taille/2), text="?", font="Arial 20 italic", fill="black")
				canvas.pack()
			elif mat_alea[i][j] == 1:
				canvas.create_text(i*taille +(taille/2), j*taille + (taille/2), text="1", font="Arial 20 italic", fill="red")
				canvas.pack()
			else:
				canvas.create_text(i*taille +(taille/2), j*taille + (taille/2), text="0", font="Arial 20 italic", fill="blue")
				canvas.pack()



def commandes_partie():
	#print('taille: {}'.format(taille))
	# on supprime le frame2
	taille = int(Entry.get(entree0))
	nom_att, nom_def = str(Entry.get(entree1)), str(Entry.get(entree2))

	faire_mat(taille)
	Frame2.pack_forget()
	# on refait le meme frame
	Frame2_bis = Frame(fenetre, borderwidth=2, relief=GROOVE)
	Frame2_bis.pack(side=RIGHT, expand='yes', padx=30, pady=100)

	# choisir entre 0 et 1
	# refaire cette partie avec un bouton 0 et un bouton 1
	b0 = Radiobutton(Frame2_bis, text='0', command=set_val_nv_pion, relief=SUNKEN)
	b0.pack(padx = 20, pady = 20)
	b1 = Radiobutton(Frame2_bis, text='1', command=set_val_nv_pion, relief=SUNKEN)
	b1.pack(padx = 20, pady = 20)

	# choisir ligne et colonne	
	# partie a refaire c'est mauvais

	# valider son choix (engage le tour de l'adversaire)
	choix = Button(Frame2_bis, text="Valider", command=nothing_for_now)
	choix.pack(side=BOTTOM, padx=10, pady=10)


# ce que contient le frame2 avant de lancer la partie
value0 = IntVar()
value0.set(4)
value1, value2 = StringVar(), StringVar() 
value1.set('Attaquant'), value2.set('Défenseur')

# on demande la taille de la matrice et le nom des joueurs
entree0 = Entry(Frame2, textvariable=value0, width=10)
entree0.pack(padx= 20, pady=20)
entree1 = Entry(Frame2, textvariable=value1, width=30)
entree1.pack(padx= 20, pady=20)
entree2 = Entry(Frame2, textvariable=value2, width=30)
entree2.pack(padx= 20, pady=20)

bouton = Button(Frame2, text="Valider", command=commandes_partie).pack()




# def creer():
# 	mat = [[1,'?',0,0],[0,1,'?','?'],['?',1,0,1],['?','?',1,0]]
# 	n= int(entree.get())
# 	# on récupère les valeurs des différents boutons et on les traite en csq (maj mat, changement display pour adversaire)
# 	canvas = Canvas(Frame1, width=n*90, height=n*90, background='beige')
# 	for i in range(n+1):
# 		ligne = canvas.create_line(i*90 +1, 0, i*90 +1, n*90 +1)
# 		canvas.pack()
# 	for i in range(n+1):
# 		ligne = canvas.create_line(0, i*90 +1, n*90 +1, i*90 +1)
# 		canvas.pack()

# 	for i in range(n):
# 		for j in range(n):
# 			if mat[i][j] == '?':
# 				b = Button(Canvas, text ="truc", relief=FLAT)
# 				canvas.coords(b, 0, 0, i*90 +50, j*90 +45)
# 				b.pack()
# 				txt = canvas.create_text(i*90 +50, j*90 +45, text="?", font="Arial 20 italic", fill="black")
# 				canvas.pack()
# 			elif mat[i][j] == 1:
# 				b = Button(Canvas, text ="truc", relief=FLAT)
# 				canvas.coords(b, 0, 0, i*90 +50, j*90 +45)
# 				b.pack()
# 				txt = canvas.create_text(i*90 +50, j*90 + 45, text="1", font="Arial 20 italic", fill="red")
# 				canvas.pack()
# 			else:
# 				b = Button(Canvas, text ="truc", relief=FLAT)
# 				canvas.coords(b, 0, 0, i*90 +50, j*90 +45)
# 				b.pack()
# 				txt = canvas.create_text(i*90 +50, j*90 + 45, text="0", font="Arial 20 italic", fill="blue")
# 				canvas.pack()


fenetre.mainloop()
