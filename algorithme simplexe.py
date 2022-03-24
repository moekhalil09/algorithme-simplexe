import sys 


def negative(a): # Retourner un vecteur negative 
	for i in range(len(a)):
		a[i]=-a[i]

def negative_mat(a):# Retourner une matrice  negative
	for i in range(len(a)):
		for j in range(len(a[i])):
			a[i][j]=-a[i][j]

def affiche(a):#Afficher une matrice
	for i in range(len(a)):
		for j in range(len(a[i])):
			num=str(format(a[i][j],".2f"))
			print('\t{}'.format(num),end="  ")
		print("\n")
			
def mat_line_division(a,p,indice):#Diviser la ligne de pivot sur le  pivot
	for i in range(len(a)):
		for j in range(len(a[i])):
			if i==indice:
				f=a[i][j]/p
				if f==0:
					a[i][j]=0
				else:
					a[i][j]=f

def mat_col_zero(a,indicey,indicex):# Rendre tous les valeurs de la colonne pivot a 0
	for i in range(len(a)):
		for j in range(len(a[i])):
			if i!=indicey:
				if j==indicex:
					a[i][j]=0
		
def col_max(a,par):#Retourner l'indice de la colonne qui contient le max
	indice=0
	maxx=a[0]
	if par=='max':
		for i in range(1,len(a)):
			if a[i]>maxx:
				maxx=a[i]
				indice=i
	else:
		for i in range(1,len(a)):
			if a[i]<maxx:
				maxx=a[i]
				indice=i
	return indice 

def line_min_sup_a_zero(a):#Retourner la valeur min sup a 0 de la colonne b/cp
	for i in range(len(a)):
		if a[i]>0:
			indice=i
			minn=a[i]
			break
	for j in range(i+1,len(a)):
		if a[j]<minn and a[j]>0:
			indice=j
			minn=a[j]
	try:
		return indice
	except:
		return 'error'

def creat_ecarts_mat(a):#Cree une matrice des valeurs d'ecarts 
	l=[]
	
	
	for i in range(len(a)):
		l.append([])
		for j in range(len(a)):
			l[i].append(j)
			if i==j:
				l[i][j]=1
			else:
				l[i][j]=0
			
	return l

def creat_mat(a,c,b,con):# Concaténer la matrice des variables  d'ecarts avec la matrice des contraintes et le vecteur b 


	for i in range(len(a)):
			lenn=len(a[i])
			for j in range(lenn+len(con[i])):
				if j>=lenn and j<=lenn+len(con[i]):
					a[i].append(con[i][j-lenn])			
	a.append([])
	for i in range(len(c)):
		a[len(a)-1].append(c[i])

	for i in range(len(a)):
		for j in range(len(a[i])):
			if j==len(a[i])-1:
				a[i].append(b[i])
			
	return a

def add_zero(a,nbr):# Ajouter des zeros sur la lignes de z
	for i in range(len(a),len(a)+nbr):
		a.append(0)
	return a



def check_vect_negatif(a,parr):
	b=1
	#verifier si tous les valeurs d'un vecteurs > 0 ou =0  dans le cas de maximisation 
	if parr=='max':
		for i in range(len(a)):
			if a[i]>0:
				b=0
				break
	#verifier si tous les valeurs d'un vecteurs < 0 ou =0 si dans le cas de minimisation
	if parr=='min':
		for i in range(len(a)):
			if a[i]<0:
				b=0
				break
	return b

def deviision_ligne_par_ligne(a,b):#la division entre deux vecteurs 
	c=[]
	if len(a)==len(b):
		for i in range(len(a)):
			try:
					f=a[i]/b[i]
					if f==0:
						c.append(0)

					else:
						c.append(a[i]/b[i])
			except:
				c.append(0)
		return c
	else:
		print(" la dimension du premier vectuer deffirente avec  celle du deuxieme")

def get_col_from_mat(a,indice):# Retourner une colonne a partir d'une matrice 
	c=[]
	for i in range(len(a)):
		for j in range(len(a[i])):
			if j==indice:
				c.append(a[i][j])
	return c

def get_last_line_from_mat(a):#Retourner la derniere ligne d'une matrice
	c=[]
	for i in range(len(a)):
		for j in range(len(a[i])):
			if i==len(a)-1:
				c.append(a[i][j])
	return c

def append_col_k(a,k):
	for i in range(len(a)):
		for j in range(len(a[i])):
			if j==len(a[i])-1:
				a[i].append(k[i])
	return a

def find_coef(a,indice_X):#cette fonction pour trouver les coefficients de chaque ligne pour passer au tableau suivant
	c=[]
	for i in range(len(a)):
		if i ==indice_Y:
				c.append("null")
		else:
			for j in range(len(a[i])):
				if j==indice_X:
					try:
						c.append(-a[i][j])
					except:
						c.append("null")

	return c

def nouvelle_matrice(a,indice_Y,indice_X,coefs):# Calculer  la matrice suivante 
	for i in range(len(a)):
		for j in range(len(a[i])):
			if i!=indice_Y:
				if j!=indice_X:
						if coefs[i]!="null":
							a[i][j]=a[indice_Y][j]*coefs[i]+a[i][j]
	return a

def abs(a):#Retourner la valeurs absolue d'un nombre 
	if a>0:
		return a
	else:
		return -a


#manipulation de la  fonction objectif		
while 1:
	fonction=str(input('\n donner la fonction objectif :\nexemple:\n\t (min ou max) z=5X1+5X2+3X3 ====>> (min ou max)5 5 3 \n\t\t\t'))
	try:
		objectif=fonction.split(' ')
		c=[]
		if objectif[0] =='min' or objectif[0] =='max':
			if len(objectif) <= 2:
				raise Exception
			for i in range(1,len(objectif)):
				c.append(int(objectif[i]))
			break
							
		else:
			print('min ou max se trouve pas dans votre fonction ...!!!')
	except:
		print("\n **** **** veuillez suivre l'exemple ci dessus  et bien fait attention sur les espaces **** ****\n\n")

#manipulation des contraintes		
while 1:
	par=str(input("\n\n donner l'ensemble des contraintes \n exemple : \n\t1X1+3X2 +1X3<=3\n\-X1+3X3<=2\n\t2x1-1X2+2X3<=4       ====>>1 3 1,-1 0 3,2 -1 2;3 2 4\n\tX1,X2,X3>=0.\n"))
	
	try:
				b=[]	
				a=[]
				parr=par.split(';')
				contraints=parr[0]
				bb=parr[1].split(' ')
		
				for i in bb:
					b.append(float(i))
				
				cont=contraints.split(',')

				if len(cont) != len(b):
					raise Exception
				
				for i in range(0,len(cont)):
					cont_l=cont[i].split(' ')
					
		
					if len(cont_l) != len(objectif)-1:
						
						raise Exception
					else:
						a.append([])
						for j in range(0,len(cont_l)):
							a[i].append(float(cont_l[j]))		
			
				break
	except:
			print("\n************veuillez suivre l'exemple ci dessus  et bien fait attention sur les espaces et les vergules et le ; et enfin la longueur des contraintes *****************")

	
#realisation du travail

if objectif[0]=='min':
		#si on est dans le cas de minimisation alors on doit mltiplie tous les contraintes  *-
		negative_mat(a)
		negative(b)
	
b.append(0)#on ajoute un 0 pour le vecture b pour 
c=add_zero(c,len(a))#on ajoute des 0 pour le vecteur c		
variables= creat_ecarts_mat(a)#on cree la matrice des variables d'ecarts
matrice=creat_mat(a,c,b,variables)#on concatène la matrice des contraintes avec la matrice des variables d'ecarts et on cree la matrice finale

print("\n\nvoici le tableau 0 :\n ")
affiche(matrice)

compt=0
base_final={}

try:
	while check_vect_negatif(c,objectif[0]) ==0:
		compt =compt+1
		indice_X=col_max(c,objectif[0])#retourner l'indice de la colonne qui contient la valeur max dans le cas de maximisation ,ou bien le min dens le cas de minimisation

		cp=get_col_from_mat(matrice,indice_X)#retourner la colonne de pivot
		b=get_col_from_mat(matrice,len(a[1])-1)#retourner la colonne b

		k=deviision_ligne_par_ligne(b,cp)#calculer le vecteur b/cp
		print("b/cp={}".format(k))

		indice_Y=line_min_sup_a_zero(k)#retourner l'indice de la ligne qui contient la valeur min sup a 0

		base_final[indice_X]=indice_Y
		
		print("le pivot = {}".format(matrice[indice_Y][indice_X]))

		mat_line_division(matrice,matrice[indice_Y][indice_X],indice_Y)#on divise la lgine pivot sur le pivot
		
		coefs=find_coef(a,indice_X)#on cherche les coefficient de chasue ligne pour calculer les nouvelles lignes
		
		nouvelle_matrice(matrice,indice_Y,indice_X,coefs)#calculer la nouvelle matrice 
		
		mat_col_zero(matrice,indice_Y,indice_X)#rendre tous la valeurs de calonne pivot a 0

		print("\n\n\nvoici le tableau:{}:\n ".format(compt))
		affiche(matrice)

		c=get_last_line_from_mat(matrice)#c resoit la derniere ligne de la mtrice 

	b=get_col_from_mat(matrice,len(a[1])-1)#retourner tous les valeurs de la colonne b lorsque on se trouve sur le dernier tableau

	print("\n\n\n")
	for i in base_final.keys():
			print("X{} ={}".format(i+1,b[base_final[i]]))
	if objectif[0]=="max":
		print("la solution optimale == {}".format(abs(b[len(b)-1])))
	else:
		print("la solution optimale == {}".format(-b[len(b)-1]))
except:
	print("ce problème n'a pas de solution")
