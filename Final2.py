# -*- coding: utf-8 -*-
from tkinter import *
import tkinter.font as tkFont
from timeit import default_timer
from random import*
import os.path
import pickle
from tkinter import messagebox

#_______________________CREATION DE VARIABLES DONT ON AURA BESOIN._________________________

niveau=0
niveau=0
boutton=0
dico_avatar,dico_fond=[],[]
nom_utilisateur=""
masquer_fenetre=0
nombre_chance=10
mot_deviner=""
mot_trouve=""
score='0000'
liste_niveau=[]  
bouton=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
alphabet_mot=[]
d=[]
y=0
listeboutons=[]
niveau_facile=[]
niveau_intermediaire=[]
niveau_difficile=[]
compteur,compteur_final=0,0
classement_des_scores=[]
classement_des_noms=[]

# Le code est à lire de bas en haut.

#_____________________TROSIEME FENETRE__________________

def recup_nom(): # fonction qui permet de récupérer le pseudo/nom de l'utiilisateur.
	global nom_utilisateur
	nom_utilisateur=demande_nom.get()
	if nom_utilisateur=="":
		nom_utilisateur="Joueur 1" # nom de l'utilisateur par défaut si aucun pseudo n'est entré.

def classement():
	global pseudo_score,classement_des_noms,classement_des_scores
	classement_des_scores=[]
	classement_des_noms=[]
	if os.path.exists('donnees'): # Le fichier existe
		f = open('donnees',"rb") #On ouvre le fichier
		pseudo_score=pickle.load(f)# On recupère le dico dans donnees contenant les pseudos avec les scores correspondants
		sred = sorted(pseudo_score.items(), key=lambda value: value[1])# On trie le dico par ordre décroissant
		for pseudo,score in pseudo_score.items():
			classement_des_noms.append(pseudo)# On rajoute dans la liste classement_des_noms les pseudos 
			classement_des_scores.append(score)# On rajoute dans la liste classement_des_score les scores 
									 
def recup_ancien_score():
	global score
	global pseudo_score
	global nom_utilisateur
	if os.path.exists('donnees'): # Le fichier existe
		# On le récupère
		f = open('donnees',"rb")
		pseudo_score=pickle.load(f)#On recupère le dico dans donnees contenant les pseudos avec les scores correspondants
		if nom_utilisateur in pseudo_score.keys():
			score=int(pseudo_score[nom_utilisateur])#On récupère le score correspondant au nom d'utilisateur si son nom est deja dans le fichier donnees
		else:
				score='0000'#Sinon on lui créé un score initialiser à 0 
				pseudo_score[nom_utilisateur]=score#on lui créer un pseudo et un score dans le dictionnaire
				
		f.close()
	else: # Le fichier n'existe pas
		score='0000'#On initialise le score à 0
		pseudo_score={}#On créer un dico pseudo_score
		pseudo_score[nom_utilisateur]=score#On rajoute dans le dico le nom d'utilisateur avec le score à 0 correspondant


def enreg_score():
	global pseudo_score
	global nom_utilisateur
	global score
	if os.path.exists('donnees'): # Le fichier existe
		# On le récupère
		f = open('donnees',"rb")
		pseudo_score=pickle.load(f)#On recupère le dico dans donnees contenant les pseudos avec les scores correspondants 
		f.close()
		pseudo_score[nom_utilisateur]=int(score)#On récupère le score en type entier
		f = open('donnees', "wb") # On écrase les anciens scores
		pickle.dump(pseudo_score,f)
		f.close()

	else:
		pseudo_score={}#le fichier n existe pas, on créer un dico pseudo_score
		pseudo_score[nom_utilisateur]=int(score)#On créé un nom d'utilisateur au joueur dans le dico avec le score qu'il a réalisé
		f = open('donnees', "wb") # On écrase les anciens scores
		pickle.dump(pseudo_score,f)#On dépose le dico dans le ficher donnees
		f.close()


# Fonctions gérant les éléments saisis par l'utilisateur
def avatar():
	global dico_avatar,dico_fond
	Avatar_1=PhotoImage(file="Image/1.gif")
	Avatar_2=PhotoImage(file="Image/2.gif")
	Avatar_3=PhotoImage(file="Image/3.gif")
	Avatar_4=PhotoImage(file="Image/4.gif")
	Avatar_5=PhotoImage(file="Image/5.gif")
	fond1=PhotoImage(file="Image/1499730799-pendue.gif")
	fond2=PhotoImage(file="Image/Cemetery_Wolves_Gothic_Fantasy_by_Mr-Ripley_Cross_527820_1280x719.gif")
	img=PhotoImage(file="Image/circle-1544536_960_720.gif")
	img2=PhotoImage(file="Image/Ligne-de-separation.gif")
	img3=PhotoImage(file="Image/square-frame-11526207112sccmzpuzkp.gif")
	dico_avatar=[Avatar_1,Avatar_2,Avatar_3,Avatar_4,Avatar_5]
	dico_fond=[fond1,fond2,img,img2,img3]

def valider():
	recup_nom()
	#score_fct()
	creation_fenetre2(dico_fond[1])
	fenetre.withdraw() #permet de cacher la première fenetre (choix du pseudo, avatar...)
					   #pour afficher la deuxième fenetre
		
def bou1(): # affectation d'un certain nombre en fonction de l'avatar choisi par l'utilisateur.
	global boutton
	boutton=1
	choix_boutton()

def bou2():
	global boutton
	boutton=2
	choix_boutton()

def bou3():
	global boutton
	boutton=3
	choix_boutton()

def bou4():
	global boutton
	boutton=4
	choix_boutton()

def bou5():
	global boutton
	boutton=5
	choix_boutton()

def choix_boutton(): #permet de changer la couleur du bouton
	for i in range(len(liste_boutton)):
		liste_boutton[i].configure(bg="WHITE") #tous les boutons sont en blancs au début
	liste_boutton[boutton-1].configure(bg="RED") #le bouton cliqué devient rouge. On commence à -1 car la liste
												 # commence à 0.
													 

#__________________________________DEUXIEME FENETRE_____________________________________

def creation_fenetre2(fond2): 

	def niv_fac(): # creation des fonctions pour les niveaux, affectation d'un certain nombre en fonction
				   # du niveau choisi par l'utilisateur.
			global niveau
			niveau=1
			choix_niveau(liste_niveau)
	def niv_int():
			global niveau
			niveau=2
			choix_niveau(liste_niveau)
	def niv_dif():
			global niveau
			niveau=3
			choix_niveau(liste_niveau)
	def choix_niveau(liste):
		for i in range(len(liste)):
			liste[i].configure(bg="ORANGE") # tous les boutons sont en orange au début
		liste[niveau-1].configure(bg="RED") # le bouton cliqué devient rouge. On commence à -1 car la liste
											# commence à 0.
	def valider2():
		global masquer_fenetre
		if niveau==0:
			messagebox.showerror("Erreur", "Veuillez sélectionner un niveau")
		else:
			creation_fenetre3(dico_fond[2],dico_fond[3]) # images de fonds utilisés en paramètre
			masquer_fenetre=1 # affecte la valeur 1 à masquer_fenetre (au début = 0). Masquer_fenetre prend la valeur 0
							  # si aucun niveau n'a été sélectionné. Si la valeur 0 est resté, c'est que l'utilisateur 
							  # n'a pas cliqué sur un bouton niveau.
			fenetre2.withdraw() #.withdraw() permet de cacher la deuxième fenetre (choix niveau).
	
	#-----Caractéristiques de la deuxième fenetre :
			 
	fenetre2=Toplevel() # permet de se focaliser, porter l'attention sur la deuxième fenetre 
	fenetre2.grab_set() 
	fenetre2.focus_set() 
	fond_c2=Canvas(fenetre2,width=735,height=500)
	fond_c2.create_image(295,253,image=fond2) #image de fond de la deuxième fenetre.
	fenetre2.resizable(width=False,height=False) # ne permet pas de redimensionner la fenetre.
	
	# création des boutons niveau facile, intermédiaire et difficile.
	niv_facile_boutton=Button(fenetre2,text="Facile",font="Forte 20", command=niv_fac,bg="DARK ORANGE",width=15)
	niv_intemerdiaire_boutton=Button(fenetre2, text="Intermédiaire",font="Forte 20", command=niv_int,bg="DARK ORANGE",width=15)
	niv_difficile_bouton=Button(fenetre2,text="Difficile",font="Forte 20",command=niv_dif,bg="DARK ORANGE",width=15)
	
	# on rajoute dans les listes qui correspondent à chaque niveaux les mots de chaque niveau. 
	liste_niveau.append(niv_facile_boutton),liste_niveau.append(niv_intemerdiaire_boutton),liste_niveau.append(niv_difficile_bouton)
	bt_valider2=Button(fenetre2,text="Valider",font="Consolas 14",command=valider2,fg="WHITE",bg="BLUE",width=12)
	niv_facile_boutton.place(x=250,y=150)
	niv_intemerdiaire_boutton.place(x=250,y=220)
	niv_difficile_bouton.place(x=250,y=290)
	bt_valider2.place(x=605,y=460)
	fond_c2.pack()


#___________________________CREATION DE LA TROISIEME FENETRE___________________________________________


def creation_fenetre3(img,img2): 
	
	def creation_dico_mot():
		f=open("1.txt",'r') #On va lire le fichier .txt
		c="" #On créer une variable c de type str qui contiendra tous les caractères du fichier.txt
		for ligne in f: #On parcours toutes les lignes dans f
			c=c+ligne #On met dans la variable c toutes les lignes de f
		f.close()
		a=c.split()
		i=0
		while i!=len(a): # en fonction de la longueur du mot, attribuer un niveau spéicifique :
			if len(a[i])<=6: # si le mot fait au plus 6 lettres, c'est le niveau facile
				niveau_facile.append(a[i]) # l'ajouter dans la liste niveau_facile qui nous servira plus tard.
				i=i+1	# incrémentation.
			elif 6<len(a[i])<=10: # si le mot fait entre 6 et 10 lettres, c'est le niveau intermédiaire.
				niveau_intermediaire.append(a[i]) # l'ajouter dans la liste niveau_intermediaire qui nous servira plus tard.
				i=i+1 # incrémentation.
			else:	# # si le mot fait plus de 10 lettres, c'est le niveau difficile.
				niveau_difficile.append(a[i]) # l'ajouter dans la liste niveau_difficile qui nous servira plus tard.
				i=i+1

	def choix_mot():	# choix du mot que l'utilisateur devinera en fonction du niveau cliqué
		global mot_deviner,mot_trouve
		if niveau==1:	# comme le bouton niveau facile est associé au nombre 1, on choisira un mot au hasard dans la liste niveau_facile
			mot_deviner=choice(niveau_facile)	
			mot_deviner=mot_deviner.upper()
		elif niveau==2: # comme le bouton niveau intermédiaire est associé au nombre 2, on choisira un mot au hasard dans la liste niveau_intermédiaire
			mot_deviner=choice(niveau_intermediaire)
			mot_deviner=mot_deviner.upper()
		elif niveau==3: # comme le bouton niveau difficile est associé au nombre 3, on choisira un mot au hasard dans la liste niveau_difficile.
			mot_deviner=choice(niveau_difficile)
			mot_deviner=mot_deviner.upper()	
		
	def updateTime(): # création du chronomètre.
		now = default_timer() - start # prend le temps par défaut, à ce moment là, que l'on soustrait à start qui est aussi la valeur par défault
									  # permet donc d'initialiser la variable à 0h 00 min 00 s.
		minutes, seconds = divmod(now, 60) # permet de compter en base de 60
		hours, minutes = divmod(minutes, 60)
		str_time = "%d:%02d:%02d" % (hours, minutes, seconds) #séparation en heure, minute et secondes.
		fond_c3.itemconfigure(text_clock, text=str_time,font =my_font3) # permet de créer l'horloge : 00:00:00
		fenetre3.after(1000, updateTime) #création d'un widget dynamique qui permet d'initialiser le widget à chaque seconde, màj à chaque seconde.

	def trace_pendu(nombre_chance): # création du dessin du pendu en fonction du nombre de chances restants à l'utilisateur
		if nombre_chance<=9:
			dessin_pendu.create_line(50,390,250,390,width=4)
		if nombre_chance<=8:
			dessin_pendu.create_line(150,390,150,100,width=4)
		if nombre_chance<=7:
			dessin_pendu.create_line(150,100,300,100,width=4)
			dessin_pendu.create_line(150,145,200,100,width=4)
		if nombre_chance<=6:
			dessin_pendu.create_line(300,100,300,150,width=4)
		if nombre_chance<=5:
			dessin_pendu.create_oval(270,150,330,200,width=4)
		if nombre_chance<=4:
			dessin_pendu.create_line(300,200,300,290,width=4)
		if nombre_chance<=3:
			dessin_pendu.create_line(300,210,270,250,width=4)
		if nombre_chance<=2:
			dessin_pendu.create_line(300,210,330,250,width=4)
		if nombre_chance<=1:
			dessin_pendu.create_line(300,290,265,330,width=4)
		if nombre_chance<=0:
			dessin_pendu.create_line(300,290,335,330,width=4)

	def mot_afficher(): # permet de savoir à quel moment l'utilisateur a réussi à deviner le mot ou pas
		global mot_trouve
		mot_trouve=""
		for lettre in mot_deviner: # pour chaque lettre dans le mot qui a été tiré au sort
			if lettre in alphabet_mot: # si la lettre dans l'alphabet
				mot_trouve=mot_trouve+lettre
			else:
				mot_trouve=mot_trouve+"-"

	def affichage_mot_deviner(): # permet d'afficher la lettre à la place du tiret correspondant
		global d
		mot_deviner_frame=LabelFrame(fenetre3, width=1080, height=40,bd=0)    
		r=0
		for i in mot_deviner:
			d.append(r)
			r=r+1
		t=0
		for i in range (len(mot_deviner)):
			d[i]=Label(mot_deviner_frame, text='-',width=5,bg="BEIGE",font="Arial 20")
			d[i].place(x=540-(len(mot_deviner)*30)+t,y=7)
			t=t+60 # permet de placer les labels pour éviter les superpositions
			
		mot_deviner_frame.place(x=0,y=160)
	
	def creation_boutton(cadre): # permet de créer les 26 boutons de l'alphabet
		for i in range(0,26):
			if i%6==0:
				y=0
			if i<6: # création des 6 première lettres
				bouton[i]=Button(cadre, text=alphabet[i],bd=5,width=8,padx=12,pady=12,command=lambda x=i: change(x),disabledforeground="BLACK")
											#disabledforegournd permet de désactiver le bouton une fois cliqué, sa couleur reste noire
				bouton[i].grid(row=0,column=y)
			if 6<=i<12: # création des 6 prochaines ect...
				bouton[i]=Button(cadre, text=alphabet[i],bd=5,width=8,padx=12,pady=12,command=lambda x=i: change(x),disabledforeground="BLACK")
				bouton[i].grid(row=1,column=y)
			if 12<=i<18:
				bouton[i]=Button(cadre, text=alphabet[i],bd=5,width=8,padx=12,pady=12,command=lambda x=i: change(x),disabledforeground="BLACK")
				bouton[i].grid(row=2,column=y)
			if 18<=i<24:
				bouton[i]=Button(cadre, text=alphabet[i],bd=5,width=8,padx=12,pady=12,command=lambda x=i: change(x),disabledforeground="BLACK")
				bouton[i].grid(row=3,column=y) 
			if 24<=i<=25: # il ne reste plus que y et z sur la cinquième ligne
				bouton[i]=Button(cadre, text=alphabet[i],bd=5,width=8,padx=12,pady=12,command=lambda x=i: change(x),disabledforeground="BLACK")
				bouton[i].grid(row=4,column=y+2)

			listeboutons.append(bouton[i])
			y=y+1

	def change(i):
		global nombre_chance,compteur_final
		if mot_deviner!=mot_trouve and nombre_chance>0: # si le mot deviné est différent du mot trouvé et si le nombre
														# de chances supérieur à 0 (l'utilisateur n'a pas encore joué)
			if alphabet[i] in mot_deviner: 
				listeboutons[i].config(bg='light green') # pour chaque lettre de l'alphabet qui se situe dans le mot à deviner
														 # le bouton devient vert
				bouton[i].configure(state='disabled')	 # une fois  cliqué, le bouton est désativé, pour limiter les bugs
				alphabet_mot.append(alphabet[i])		 # rajout dans une liste que l'on utilisera pour savoir si l'utilisateur
														 # a déjà trouvé le même mot.
				mot_afficher()							 # appel à une fonction qui permet d'afficher le mot
			else:										 # si la lettre n'est pas dans le mot à deviner 
				listeboutons[i].config(bg='red')		 # le bouton devient rouge
				bouton[i].configure(state='disabled')	 # une fois cliqué, le bouton est désactivé, pour limiter les bugs
				nombre_chance=nombre_chance-1			 
				trace_pendu(nombre_chance)				 # traçage du pendu
			
		n=0	 # initialisation des rangs à 0
		while n !=len(mot_deviner): # tant que n est différent de la longueur du mot à deviner :
			if alphabet[i]==mot_deviner[n]: # si la lettre de l'aphabet est dans le mot à deviner
				d[n].config(text=alphabet[i]) # on change le tiret correspondant par la lettre
				
				n=n+1 # incrémentation
			else: # si la lettre n'est pas dans le mot à deviner
				n=n+1 # on incrémente tout simplement.

		if nombre_chance==0:	# si le nombre de chance = 0, l'utilisateur perd
			compteur_final=compteur # permet d'arrêter le chrono, sauvegarde du temps à l'instant même
			dessin_pendu.configure(bg="RED") # le canva devient rouge
			fenetre_defaite_fct(dico_fond[2],dico_avatar[boutton-1]) # images de fond en paramètre
		elif mot_deviner==mot_trouve: # si l'utilisateur a gaggné :
			compteur_final=compteur # permet d'arrêter le chrono, sauvegarde du temps à l'instant même
			dessin_pendu.configure(bg="GREEN") # le canva devient vert
			attribution_score(niveau) # donner un score à la personne 
			fenetre_victoire(dico_fond[2],dico_avatar[boutton-1]) #fenetre victoire s'affiche avec utilisation de fonds

	
#---------CREATION D'UN SYSTEME DE CLASSEMENT DANS LA TROISIEME FENETRE


	def affichage_classement(fenetre): # permet de créer 3 listes dans lesquelles on va rajouter autant d'élément 
									   # qu'il y en a dans la liste classement_des_noms
		global classement_des_noms,pseudo_score,classement_des_scores
		c=[]
		e=[]
		f=[]
		x=1
		y=1
		classement_frame=LabelFrame(fenetre,width=1080,height=4,bd=10)
		r=0
		for i in classement_des_noms:
			c.append(r)
			e.append(r)
			f.append(r)
			r=r+1 # on incrémente r pour avoir des éléments différents 
		for i in range(len(classement_des_noms)): # Pour chaque valeur dans classement_des_noms
			c[i]=Label(classement_frame, text=classement_des_noms[i], width=10, bg='BEIGE', font='Arial 20')
				# On prend chaque élément de la liste c et on créerpour chacun un label qui affichera le nom du joueur.
			c[i].grid(row=x,column=1)
			e[i]=Label(classement_frame, text=classement_des_scores[i], width=10, bg='BEIGE', font='Arial 20')
				# On prend chaque élément de la liste e et on crée pour chacun un label qui affichera le score du joueur.
			e[i].grid(row=x,column=2)
			e[i]=Label(classement_frame, text=x, width=10, bg='BEIGE', font='Arial 20')
				# On prend chaque élément de la liste e et on crée pour chacun un label qui affichera le rang du joueur.
			e[i].grid(row=x,column=0)
			x=x+1 # on incrémente x, pour qu'il ne reste pas à 1.

		# placements des labels qui correspondent chacun au texte "Rang", "Joueur" et "Score".
		rang=Label(classement_frame, text='Rang', width=10, bg='BEIGE', font='Arial 20',bd=10)
		rang.grid(row=0,column=0)
		Joueur=Label(classement_frame, text='Joueur', width=10, bg='BEIGE', font='Arial 20',bd=10)
		Joueur.grid(row=0,column=1)
		Score=Label(classement_frame, text='Score', width=10, bg='BEIGE', font='Arial 20',bd=10)
		Score.grid(row=0,column=2)
		classement_frame.place(x=120,y=250) # placemment du classement des 3 premiers

	def affichage_3_premiers():
		global classement_des_noms,pseudo_score,classement_des_scores # même principe ici.
		c=[]
		e=[]
		f=[]
		x=1
		y=1
		classement_frame=LabelFrame(fenetre3,width=1080,height=4,bd=10,bg="BEIGE")
		r=0
		for i in classement_des_noms:
			c.append(r)
			e.append(r)
			f.append(r)
			r=r+1
		if len(classement_des_noms)>=3: # s'il y a plus de 3 éléments dans classement_des_noms
			for i in range(0,3): # On n'a affiche que les 3 premiers éléments .
				c[i]=Label(classement_frame, text=classement_des_noms[i], width=10, bg='BEIGE', font='Arial 10')
				c[i].grid(row=x,column=1)
				e[i]=Label(classement_frame, text=classement_des_scores[i], width=10, bg='BEIGE', font='Arial 10')
				e[i].grid(row=x,column=2)
				e[i]=Label(classement_frame, text=x, width=10, bg='BEIGE', font='Arial 10')
				e[i].grid(row=x,column=0)
				x=x+1 # on incrémente le rang de sorte que ça ne reste pas à 1.
				
				# placements des labels qui correspondent chacun au texte "Rang", "Joueur" et "Score".
				rang=Label(classement_frame, text='Rang', width=10, bg='BEIGE', font='Arial 10',bd=10)
				rang.grid(row=0,column=0)
				Joueur=Label(classement_frame, text='Joueur', width=10, bg='BEIGE', font='Arial 10',bd=10)
				Joueur.grid(row=0,column=1)
				Score=Label(classement_frame, text='Score', width=10, bg='BEIGE', font='Arial 10',bd=10)
				Score.grid(row=0,column=2)
		classement_frame.place(x=420,y=10) # placemment du classement des 3 premiers

#---------CREATION D'UNE FONCTION PRINCIPALE


	def fonction_principale(start): # pour ne pas réécrire les 8 fonctions.
		creation_dico_mot()
		choix_mot()
		affichage_mot_deviner()
		creation_boutton(cadre_boutton)
		updateTime()
		incremente()
		classement()
		affichage_3_premiers()
		
	def incremente(): #création d'une variable compteur qui s'incrémente en même temps que le chrono 
					  # pour récupérer le temps.
		"Incrémente le compteur à chaque seconde"
		global compteur
		compteur += 1
		fenetre3.after(1000, incremente)

	def attribution_score(niveau): # permet de donner un scrore à l'utilisateur 
		global score
		score=int(score)
		recup_ancien_score()
		score=int(score)
		if compteur_final<30: # le score dépend du temps qu'a mis l'utilisateur à trouver ou non le mot à deviner
			score=niveau*1000+score # en moins de 30 secondes, 1000 points
		elif compteur_final<60 and compteur_final>30: # entre 30 et 60 secondes, 500 points
			score=niveau*500+score 
		else:
			score=niveau*100+score # un temps plus grand, 100 points.
		enreg_score()
		
	fenetre3=Toplevel() # permet de se focaliser sur la troisième fenetre.
	fenetre3.grab_set() 
	fenetre3.focus_set()
	fenetre3.geometry("1080x600")
	fenetre3.resizable(width=False,height=False)
	my_font2=tkFont.Font(fenetre3,family="Cataneo BT",size=25)
	my_font3=tkFont.Font(fenetre3,family="Cataneo BT",size=35)
	fond_c3=Canvas(fenetre3,width=1080,height=600)
	cadre_boutton=LabelFrame(fenetre3, width=600, height=600,bd=0)
	
	recup_ancien_score() # on récupère les anciens scores que l'on affichera ensuite dans un
						 # petit tableau en haut de la fenêtre.
	affichage_score=Label(fenetre3,text= pseudo_score[nom_utilisateur],font=my_font2) # 
	affichage_nom=Label(fenetre3,text=nom_utilisateur,font=my_font2)
	fond_c3.create_image(80,80,image=dico_avatar[boutton-1])
	fond_c3.create_image(80,80, image=img)
	fond_c3.create_image(540,160,image=img2)
	fond_c3.create_text(200,115,text="Score:",font=my_font2)
	text_clock = fond_c3.create_text(900,90)
	dessin_pendu=Canvas(fenetre3,width="400",height="400",bd=10)
	dessin_pendu.create_image(200,225,image=dico_fond[4])
	start = default_timer()
	
	
	fonction_principale(start) # appel à la fonction start qui activera elle-même 8 autres fonctions.
	


	fond_c3.place(x=10,y=20)
	affichage_score.place(x=270,y=118)
	affichage_nom.place(x=190,y=40)
	dessin_pendu.place(x=20,y=180)
	cadre_boutton.place(x=500,y=280)

#________________________________________________________________________________________________________
	def reactiver(): # réactivation de tous les boutons, car ils étaient désactivés (disabledforeground) 
					 # pour limiter les bugs
		for k in range(26):
			bouton[k].configure(state='normal')
	
	def reinitialiser(): # réinitisation si le joueur veut rejouer : réinitialisation de toutes les variables modifiées aupravant
			global niveau,masquer_fenetre,nombre_chance,mot_deviner,mot_trouve,liste_niveau,alphabet_mot,d,y,listeboutons,compteur_final, compteur
			niveau=0 # niveau redevient 0
			masquer_fenetre=0 # aucune fenetre masquée
			nombre_chance=10 # nombre de chance réinitialisé à 10
			mot_deviner=""
			mot_trouve=""
			liste_niveau=[]  
			alphabet_mot=[]
			d=[]
			y=0
			listeboutons=[]
			compteur=0 # temps remis à 0
			compteur_final=0 # temps remis à 0
			reactiver() # fonction pour réactiver tous les boutons

	def fenetre_defaite_fct(img,img2): # si le joueur veut réessayer/rejouer
		def rejouer():
			reinitialiser() # appel de la fonction reinitialiser
			fenetre3.destroy() #destruction de la fenetre 3
			fenetre_defaite.destroy()
			creation_fenetre2(dico_fond[1]) # on retourne à la deuxième fenêtre pour refaire un choix de niveau

		fenetre_defaite=Toplevel() # fenetre pour informer que l'utilisateur a perdu
		fenetre_defaite.grab_set() 
		fenetre_defaite.focus_set() 
		fenetre_defaite.geometry("900x600") # dimensions de la fenetre_defaite
		fenetre_defaite.resizable(width=False,height=False)
		my_font2=tkFont.Font(fenetre_defaite,family="Cataneo BT",size=25)
		fond_c4=Canvas(fenetre_defaite,width=800,height=200)
		fond_c4.create_text(420,20,text="Dommage "+nom_utilisateur+" votre mot était: "+mot_deviner,font=my_font2)
		enreg_score()
		fond_c4.create_text(425,60,text="vous gagnerez une prochaine fois",font=my_font2)
		fond_c4.create_text(150,120,text="Score: ",font=my_font2)
		rejouer_bt=Button(fenetre_defaite,text="Rejouer",command=rejouer,width=10,font="Forte 20",bg="GREEN")
		quitter=Button(fenetre_defaite,text="Quitter",command=fenetre.destroy,width=10,font="Forte 20",bg="RED")
		affichage_classement(fenetre_defaite) # appel à la fonction pour pouvoir regarder le classement dans la fenetre défaite.
		affichage_score=Label(fenetre_defaite,text=score,font=my_font2)
		rejouer_bt.place(x=420,y=530)
		quitter.place(x=600,y=530)
		affichage_score.place(x=260,y=95)
		fond_c4.pack()

	
	def fenetre_victoire(img,img2): # si le joueur veut réessayer, même fonctionnement 
		def rejouer2():
			reinitialiser() # appel de la fonction reinitialiser
			#score_fct()
			recup_ancien_score() # permet de récupérer le score que le joueur a eu, pour ensuite pouvoir rejouer avec le même score.
			creation_fenetre2(dico_fond[1]) # retour à la deuxième fenêtre pour que le joueur choisisse un niveau
			fenetre3.destroy() # on détruit évidemment la troisième fenetre, puis la fenetre_victoire.
			fenetre_victoire.destroy() 
		
		fenetre_victoire=Toplevel() # permet de se focaliser sur la fenetre victoire et de laisser tomber les autres fenetre.
		fenetre_victoire.grab_set() 
		fenetre_victoire.focus_set() 
		fenetre_victoire.geometry("900x600") # dimensions de la fenetre_victoire.
		fenetre_victoire.resizable(width=False,height=False) # non redimensionnable.
		my_font2=tkFont.Font(fenetre_victoire,family="Cataneo BT",size=25)
		enreg_score()
		classement()
		fond_c4=Canvas(fenetre_victoire,width=500,height=200)
		fond_c4.create_text(250,20,text="Félicitation "+nom_utilisateur,font=my_font2)
		fond_c4.create_text(250,50,text="vous avez gagné",font=my_font2)
		fond_c4.create_text(200,120,text="Score: ",font=my_font2)
		affichage_classement(fenetre_victoire) # appel à la fonction pour pouvoir regarder le classement dans la fenetre victoire.
		rejouer_bt=Button(fenetre_victoire,text="Rejouer",command=rejouer2,width=10,font="Forte 20",bg="GREEN")
		quitter=Button(fenetre_victoire,text="Quitter",command=fenetre.destroy,width=10,font="Forte 20",bg="RED")
		affichage_score=Label(fenetre_victoire,text=score,font=my_font2)
		rejouer_bt.place(x=420,y=530)
		quitter.place(x=600,y=530)
		affichage_score.place(x=500,y=95)
		fond_c4.pack()
	
				

#_________________________________PREMIERE FENETRE (pseudo, avatar...)._________________________________
fenetre = Tk()
fenetre.title('Pendu')
fenetre.geometry("735x500")
fenetre.resizable(width=False,height=False) # fenetre impossible à redimensionner.
my_font =tkFont.Font(fenetre, family="Vivaldi",size=60, underline = 1 )

fond_c=Canvas(fenetre,width=1012,height=600) # Création d'un Canvas pour pouvoir ensuite écrire dessus.
fond = PhotoImage(file="Image/1499730799-pendue.gif")
fond_c.create_image(200, 300, image=fond) #image de fond
fond_c.create_text(367,50,text="Le pendu" ,font=my_font,fill="WHITE")
fond_c.create_text(550,140,text="Sous quel nom souhaitez-vous jouer?",font="Consolas 14",fill="BEIGE")
demande_nom=Entry(fond_c,bg="BEIGE",fg="DARK RED",font='Helvetica 18 bold',width=17) # création de l'entrée pour mettre le pseudo de l'utilisateur.
fond_c.create_text(490,230,text="Choississez un avatar:",font="Consolas 14",fill="BEIGE")

avatar()

bt_1 = Button(fenetre,image=dico_avatar[0],activebackground="GREY",command=bou1) # creation des boutons correspondont aux 5 avatars.
bt_2 = Button(fenetre,image=dico_avatar[1],activebackground="GREY",command=bou2)
bt_3 = Button(fenetre,image=dico_avatar[2],activebackground="GREY",command=bou3)
bt_4 = Button(fenetre,image=dico_avatar[3],activebackground="GREY",command=bou4)
bt_5 = Button(fenetre,image=dico_avatar[4],activebackground="GREY",command=bou5)

liste_boutton=[bt_1,bt_2,bt_3,bt_4,bt_5]
bt_valider=Button(fenetre,text="Valider",fg="WHITE",font="Consolas 14",bg="BLUE",command=valider,width=12)
bt_1.place(x=380,y=250) # placement des boutons 
bt_2.place(x=490,y=250)
bt_3.place(x=600,y=250)
bt_4.place(x=435,y=345)
bt_5.place(x=560,y=345)
bt_valider.place(x=600,y=458) 
fond_c.pack()
demande_nom.place(x=430,y=170)

fenetre.mainloop()


