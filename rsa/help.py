# encoding: utf-8

def pgcd(a,b):
    # L'algo PGCD
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

# On récupére n puis on le factorise pour obtenir les deux grands nombres premiers p et q
# La fonction factoriser avec en argument NN
def factoriser(NN):
    b = 2
    while b:
        while NN % b != 0 :
            b = b+1
        if NN/b == 1 :
            print ('\n p = ', b,)
            # On créé une variable globale p pour la réutiliser hors de la fonction et p=b
            global p
            p = b
            break
        print ('\n q = ', b,)
        # On créé une variable globale q pour la réutiliser hors de la fonction et q=b
        global q
        q = b
        NN = NN/b;

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b % a,a)
    return (g, x - (b//a) * y, y);

# Fonction modulo_inverse qui calcule le modulo inverse
def modulo_inverse(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Pas de modulo inverse');
    return x%m

print ("\n ------- Clé publique : -------")

e = 12413
print("e = ",e)
n = 13289
print("n = ",n)
factoriser(n) #Extraire p et q de n, à l'aide de la fonction factoriser


phi = (p-1)*(q-1)
print(' \n Phi  de n : ',phi,)
print (" \n Clé publique (",e,",",n,")")

while e<phi:
	if pgcd(e,phi)==1:
		break
	else:
		e+=1
	if e>=phi:
		print("Erreur"),
		sys.exit
d = modulo_inverse(e,phi)
print (" \n Clé privée (",d,",",n,")")

M = [9197, 6284, 12836, 8709, 4584, 10239, 11553, 4584, 7008, 12523, 9862, 356,
5356, 1159, 10280, 12523, 7506, 6311] 

for i in M :
    nbr_dec = pow(i,d,n)
    print("\n ----------------------------------------------")
    print("\n Le message en clair de ",i," est : ",nbr_dec,)