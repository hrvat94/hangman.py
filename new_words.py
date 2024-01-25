import sqlite3

connection = sqlite3.connect("Woche_11/db/database.db")
cur = connection.cursor()

print("Programm zum speichern von neuen Wörtern in die Datenbank wurde gestartet...")

while True:
    i = input("Welches Wort soll der Datenbank hinzugefügt werden (oder EXIT)?\n").upper()

    if i == "EXIT":
        print("Programm wurde beendet!")
        connection.close()
        break 

    #print(i)
    #print(len(i))

    data = (i, len(i))
    #print(cur.execute("SELECT * FROM words").fetchall())
    table = cur.execute("SELECT * FROM words").fetchall()
    #print(type(table))
    #print(data)
    #print(type(data))

    if data in table:
        print(f"Das Wort {i} befindet sich schon in der Datenbank!")
    else:
        cur.executemany("INSERT INTO words VALUES (?,?)", [data])
        connection.commit()
        print(f"Das Wort {i} wurde der Datenbank hinzugefügt.")
    
    