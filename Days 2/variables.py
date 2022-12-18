# Variables 
#
# A chaque varaiables creer un espace memoire qui est alloue
# Quand on affecte une valeur a une variable on parle d'afferctation


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






if __name__ ==  '__main__':
    print("Informations")
    print("------------------")
    # Permet de la sortie a la console
    print("Informations personnelle")
    # {0} implique "SAWADOGO" / {} implique "SAWADOGO"
    print("Lastname: {0} ".format(lastname))
    print("Fistname: {} ".format(firstname) )
    print("Tall: {} " .format(tall))
    print("Weight: {0}, SexType: {1} ".format(weight, sexetype))
    print("SexType: ")
    print("\n")
 
    print("********************")
    print("Informations professionnelles")
    print(f"Profession: {profession}")
    print(f"Experience: {experience} ")
    print(f"School: {school} ")
    print(f"Degre: {degre} ")
    print(f"Salary: {salary} ")
    print("\n")


    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Informations Personnelles: ")
    print("Lastname:{0}, Firstname: {1}, Tall:{2}, Weight:{3}, SexType:{4} ".format(lastname,firstname,tall,weight,sexetype))

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Informations Profesionnelles: ") 
    print(f"Profession: {profession}")

    print(f"Profession:{profession}, School:{school}, Degre:{degre}, Salary:{salary} ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
    
