import os

def palindrome(chaine: str):
    # Convert to lowercase for case insensitivity
    chaine = chaine.lower()

    # Remove spaces
    chaine = chaine.replace(" ", "")

    # Reverse the string
    chaine_inverse = chaine[::-1]

    if chaine == chaine_inverse:
        return True

    return False

string1 = "kayak"
string2 = "never odd or even"
string3 = "Was it a car or a cat"

print(palindrome(string1))  # True
print(palindrome(string2))  # True
print(palindrome(string3))  # False

def listFilesDirectory(path: str):
    print(f"Contenu de {path}:")
    for root, dirs, files in os.walk(path):
        current_directory = os.path.relpath(root, path)
        print(f"\nDossier: {current_directory}")
        
        for file in files:
            print(f" -- Fichier: {file} --")
        for dir in dirs:
            print(f" -- Sous-Dossier: {dir} --")

path = "/home/aarthur/introduction_seminar/"
listFilesDirectory(path)

