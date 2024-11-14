#coding:utf-8

# fonction qui permet de verifier si un nombre est heureux ou pas
def happy(n):  
    if n < 10: 
        n = n**2

    while n > 9:
        total = 0
        for digit in str(n):
            total += int (digit)**2
        n = total

    return n == 1 # la fonction retourne vrai si le nombre n est egal à 1 et faux sion


# fonction qui permet d'afficher les nombre heureux jusqu'a un nombre donné
def happy_interval(sup):
    happy_list = []
    print("******** LISTE DES NOMBRES HEUREUX ********\n")
    for i in range (1, sup + 1):
        if happy(i):
            print(i)
            happy_list.append(i) #insert le nombre heureux à la position i
    return happy_list 


#exemple d'application
happy_interval(100)  
