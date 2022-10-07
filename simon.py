import time
import random
import os


def clear_screen():
    if (os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')


clear_screen()

# Génération de le séquence initiale
sequence = ""
for i in range(4):
    chiffre = random.randint(0, 9)
    sequence += str(chiffre)

print("Bienvenue dans le jeu du simon")

score = 0
while True:
    print("Retenez la séquence")
    time.sleep(1)
    print(sequence)
    time.sleep(3)
    clear_screen()

    seq_user = input("Saisissez votre réponse: ")
    if seq_user == sequence:
        score += 1
    else:
        break

    chiffre = random.randint(0, 9)
    sequence += str(chiffre)
    clear_screen()

print("Mauvaise réponse")
print(f"La séquence était {sequence}")
print(f"Votre sore final est: {score}")
