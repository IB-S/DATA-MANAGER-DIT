# Operations
# Operation arithmetiques
# 


lastname = "SAWADOGO"
firstname = "Ibrahim"
profession = "Statisticien"
experience = 1
school = "UNB"
degre = "INGENIEUR"
sexetype = "M"
salary = 500000.987
tall = 175 
weight = None # NULL(undefined)
# 18. = 18.0
float_special = 18.
string_special = "500000.987"




if __name__ ==  '__main__':
    # 
    # 
    
    # Addition
    addition =  salary + tall
    print("Addition de deux nombres")
    print(addition)
    print("\n")

    # Soustraction
    soustraction = salary - tall
    inv_soustraction = tall -salary
    print(soustraction)
    print(inv_soustraction)
    print("\n")
    # Multiplication
    multiplication = tall*experience
    print("Multiplication de deux nombres:")
    print(f"le resutat est: {multiplication}")
    print("\n")
    # Division
    division = tall / experience
    print(f"le resultat est: {division}")
    print("\n")
    # Division entiere
    #
    #Affiche la partie entiere du resultat
    # float // float = int
    ent_division = salary // float_special
    print(f"le resultat est : {ent_division}")
    print("\n")
    # Exposant
    exposant_carre = experience**2
    exposant_cube = experience**3
    exposant_dix = experience**10
    print(f"Le resultat de l'exposant est: {exposant_carre}")
    print("\n") 