import sqlite3

bd =  sqlite3.connect('Basuka.db')
kluc = bd.cursor()

kluc.execute('''CREATE TABLE IF NOT EXISTS Tusa(
	id integer PRIMARY key autoincrement,
	Name text,
	Role text);''')
kluc.execute('''INSERT into Tusa(Name,Role) VALUES ('Pavel', 'leading');''')
kluc.execute('''INSERT into Tusa(Name,Role) VALUES ('Egor', 'player');''')
kluc.execute('''INSERT into Tusa(Name,Role) VALUES ('Anna', 'player');''')
kluc.execute('''INSERT into Tusa(Name,Role) VALUES ('Alina', 'Assistant');''')

kluc.execute('''select* from Tusa;''')
bd.commit()
s = kluc.fetchall()
print(s)