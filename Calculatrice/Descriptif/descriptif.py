
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

if résultat is not None:
    print("Le résultat est:", résultat)