
#On utilisera une liste dans cette section
historique = []
#La premiere partie sera introduit dans une fonction que l'on appelera "calculer()"
def calculer():
    num1 = float(input("Entrez le premier nombre: "))
    num2 = float(input("Entrez le deuxième nombre: "))
    operator = input("Entrez l'operateur souhaité (+, -, /, *): ")

    if operator == "+":
        résultat = num1 + num2
    elif operator == "-":
        résultat = num1 - num2
    elif operator == "/":
        if num2 != 0:
            résultat = num1 / num2
        else:
            print("Erreur: Impossible de diviser par zéro.!")
            résultat = None
    elif operator == "*":
        résultat = num1 * num2
    else:
        print("Erreur: Operateur non valide.")
        résultat = None

    expression = f"{num1} {operator} {num2} = {résultat}"
    historique.append(expression)

    if résultat is not None:
        print("Le résultat est:", résultat)

def afficher_historique():
    print("Historique de calculs:")
    for expression in historique:
        print(expression)

def éffacer_historique():
    historique.clear()
    print("Historique éffacé")

calculer()
afficher_historique()
éffacer_historique()