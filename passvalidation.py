import re

def validate_password(password):
    if len(password) < 8:
        return "Le mot de passe doit contenir au moins 8 characteres"

    if not re.search(r'\d', password):
        return "Le mot de passe doit contenir au moins un digits"

    if not re.search(f'[A-Z]', password):
        return "Le mot de passe doit contenir au moins une majuscule"

    if not re.search(f'[!@#$%&*_?-]', password):
        return "Le mot de passe doit contenir au moins un de ces characters:\n ! @ # $ % & * _ ? - "

    else:
        return "Bravo vous avez entre le bon mot de passe"

def demander():
    password = input("Entrez un mot de passe: ")
    return password

password = demander()
validate_result = validate_password(password)
print(validate_result)
