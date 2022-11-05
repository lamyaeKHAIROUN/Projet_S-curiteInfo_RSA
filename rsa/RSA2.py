
import random
## la fonction qui teste la primalité dun nombre 
def is_prime(n):
   

    if n == 1 or n == 2:
        return True

    if n % 2 == 0:
        return False

    r = n ** 0.5

    if r == int(r):
        return False

    for x in range(3, int(r), 2):

        if n % x == 0:
            return False

    return True

## la fonction qui genere les deux nombre premiers q et p
def generateNumbers():
    p=0
    q=0
    while is_prime(p) is not True :
        p = random.randint(10,1000)
    while is_prime(q) is not True :   
        q=random.randint(100,1000)
       
    n=p*q
    phi_n=(p-1)*(q-1)   
    return(p,q)
 
## generation du nombre e 
def pgcd(a,b):
	while b:
		a, b = b, a%b
	return a

def choisir_e(phi_n):
     e=0

     while pgcd(e,phi_n)!=1 :
        e=random.randint(1,phi_n-1)

     return e
  

# Algorithme d'Euclide etendu pour le calcule de d

def euclide_etendu(a,b):
    # Initialisation
    r,u,v,r1,u1,v1=a,1,0,b,0,1
    # Calcul
    while r1!=0:
        q=r//r1
        rs,us,vs=r,u,v
        r,u,v=r1,u1,v1
        r1,u1,v1=rs-q*r1,us-q*u1,vs-q*v1
  
    return u%b
##chiffrement
def chiffrer(msg,e,n):
  msg_ch=pow(msg,e,n)
  return msg_ch

## dechiffrement
def dechiffrer(message_chiffre, d,n):
    m=pow(message_chiffre,d,n)
    return m
###########Question 2#######################################
p,q=generateNumbers()
n=p*q
phi_n=(p-1)*(q-1)
e=choisir_e(phi_n)
d=euclide_etendu(e,phi_n)
##### main###
#message = int (input("\n saisis le message que tu veux chiffrer : "))

#c=chiffrer(message,e,n)
#print("\n###Chiffrement###\n")
#print("voila le message chiffree : ",c)
#print("la cle public : " ,e,",",n)
#print("clé privée : ",d,",",n)
    ##dechiffrement##
#print("\n###Dechiffrement###\n")
#print("le message dechiffre est : ",dechiffrer(c,d,n))


################### Question 3 #######################
#generation de la cle public
print("la cle public genere est : ", e,",",n)
#generation de la cle privee
print("la clest prv genere est : ", d)

#dechiffrer le message qui a ete crypte avec une autre machine en utilisant ma cle public
print("le message chiffre est : ",dechiffrer(1516,18303,76639))




#######################Question 4##########################"
 # La fonction de factorisation de n
def generer_p_q(n):
    b = 2
    while b:
        while n % b != 0 :
            b = b+1
        if n/b == 1 :
           # print ('\n p = ', b,)
            # On créé une variable globale p pour la réutiliser hors de la fonction et p=b
            global p
            p = b
            break
       # print ('\n q = ', b,)
        # On créé une variable globale q pour la réutiliser hors de la fonction et q=b
        global q
        q = b
        n = n/b;
    return (p,q)


##la fonction de dechiffrement avec la clé publique (e ; n)
def dechiffrer1(message_chiffre,e,n):
    #calculer d
    
    p,q=generer_p_q(n)
    phi_n=(p-1)*(q-1)
    d=euclide_etendu(e,phi_n)
    #message chiffre
    m=pow(message_chiffre,d,n)
    return m

##la permiere liste
list1 = [9197, 6284, 12836, 8709, 4584, 10239, 11553, 4584, 7008, 12523, 9862, 356,
5356, 1159, 10280, 12523, 7506, 6311] 
print("\nchiffrement avec la cle public  (12413 ; 13289): \n")
for i in list1:
    e=12413
    n=13289
    msg_dechifre=dechiffrer1(i,e,n)
    print("le message chiffre de ", i, "est : ",msg_dechifre)

##la deuxieme liste 
print("\nchiffrement avec la cle public (163119273;755918011):\n ")

list2=[671828605, 407505023, 288441355, 679172842, 180261802]
for i in list2:
    e=163119273
    n=755918011
    msg_dechifre=dechiffrer1(i,e,n)
    print("le message chiffre de ", i, "est : ",msg_dechifre)

###########Question 5###################
def crypter_mot():
    p,q=generateNumbers()
    n=p*q
    phi_n=(p-1)*(q-1)
    e=choisir_e(phi_n)
    d=euclide_etendu(e,phi_n)
    # On demande d'entrer le texte à crypter
    mot = input('\nEntrez le mot ou la phrase à crypter : ')
    # On récupère le nombre de caractères du texte.
    taille_du_mot = len(mot)
    i = 0
    # Tant que i inférieur au nombre de caractères
    while i < taille_du_mot :
        # Comme i s'incrémente jusqu'à égalité avec la taille du mot,
        #  à chaque passage dans la fonction chaque lettre sera convertie.
        ascii = ord(mot[i])
        print("code ascii : ", ascii)
        # On crypte la lettre ou plutôt son code ASCII
        lettre_crypt = chiffrer(ascii,e,n)
        
        print("lettre crypte : ",lettre_crypt)

        # Si le code ASCII est supérieur à n 
        if ascii > n :
            print ("Les nombres p et q sont trop petits veuillez recommencer.")
            # Si le bloc crypté est supérieur à phi(n)
        if lettre_crypt > phi_n :
            print ("Erreur de calcul")
        i=i+1
crypter_mot()