import sqlite3
from random import choice

connection = sqlite3.connect("Woche_11/db/database.db")
cur = connection.cursor()
MAX_VERSUCHE = 5

while True:
    print("Eine neue Runde Hangman!")
    i = input("Wähle die Anzahl der Buchstaben, welche das Wort enthalten soll. \nOder gib EXIT ein, wenn das Spiel beendet werden soll.\n")
 
    try:
        i = int(i)
        #print(i)
    except ValueError:
        if i == "EXIT" or i == "exit":
            print("Spiel wird beendet.")
            connection.close()
            break 
        else:
            print(f'Du hast {i} eingegeben, welches keine Zahl darstellt.')
            continue

    words = cur.execute(f"SELECT * FROM words WHERE letters = {i}").fetchall()

    if words:
        #print(words)
        target_word = choice(words)
        print (target_word)

        print("Ein Wort wurde ausgewählt...")
        print("Die Raterunde beginnt!")
        print(f"Du hast {MAX_VERSUCHE} Versuche, das Wort rauszufinden!")
        print("Viel Spaß!")
        print()

        list_target_letters = [*target_word[0]]
        correctly_guessed_letters = list_target_letters.copy()

        for idx, e in enumerate(correctly_guessed_letters):
            correctly_guessed_letters[idx] = "_"

        #print(list_target_letters)

        for n in range(0, MAX_VERSUCHE):
            print(*correctly_guessed_letters)
            print(f"Verbleinde Anzahl Versuche: {MAX_VERSUCHE-n}")
            guess = input("Welchen Buchstaben wählst du? \n").upper()

            if guess in list_target_letters:
                #index = list_target_letters.index(guess)
                for idx, e in enumerate(correctly_guessed_letters):
                    if list_target_letters[idx] == guess:
                        correctly_guessed_letters[idx] = guess
            else:
                print(f"{guess} ist leider nicht vorhanden...")

            if "_" not in correctly_guessed_letters:
                print("Geschafft!")
                print()
                break
            if "_" in correctly_guessed_letters and MAX_VERSUCHE-n == 1:
                print("Sie haben es leider nicht geschafft. Das Spiel wird neu gestartet...")
                print()
    else:
        print("Keine Wörter gefunden...")
    