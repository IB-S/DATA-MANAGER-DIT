# Types 
# La nature de la valeur de la variable
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
    # Permet dedeterminer le type des variables
    # Pour afficher le type: type(<variable>)
    # Toutes classe est un type en programmation
    # 
    print(type(lastname))
    print(type(salary))
    print(type(tall))
    print(type(weight))
    print(type(float_special))

# Afficher le type de sextype, experience et string_special

    print(f"Sextype: {sexetype}, Experience: {experience}, String_Special: {string_special}  ")
# 
#     
    print(f"le type de la variable lastename est: {type(lastname)}")
    print(f"le type de la variable salary est: {type(salary)}")
    print(f"le type de la variable experience est: {type(experience)}")
    print(f"le type de la variable sexetype est: {type(sexetype)}")
    print(f"le type de la variable string_special est: {type(string_special)}")

    # Declaration et assignation
    # Declaration de variables
    # Assignation de valeur

    type_salary = type(salary)
    type_lastname = type(lastname)
    type_weight = type(weight)
    type_experience =type(experience)
    type_sextype = type(sexetype)
    type_string_special = type(string_special)
    type_float_special = type(float_special)

    print(f"le type de la variable float_special est {type_float_special} " )
