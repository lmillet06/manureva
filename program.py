# -*-coding:Latin-1 -*
import os # On importe le module os
import sqlite3

# fichierDonnees ="C:/Users/emare/Desktop/EPSI B3/TOURMAN Integration continue/bd_test.sq3"
fichierDonnees ="bd_test.sq3" 
conn =sqlite3.connect(fichierDonnees)
conn.text_factory = str
cur =conn.cursor()
car =conn.cursor()

# cur.execute("CREATE TABLE membres (age INTEGER, nom TEXT, taille REAL)")
# cur.execute("INSERT INTO membres(age,nom,taille) VALUES(21,'Dupont',1.83)")
# cur.execute("INSERT INTO membres(age,nom,taille) VALUES(15,'Blumar',1.57)")
# cur.execute("INSERT Into membres(age,nom,taille) VALUES(18,'Ozemir',1.69)")

# cur.execute("DELETE FROM membres where age >1")

cur.execute("select name from sqlite_master where type = 'table'")
car.execute("select * from membres")
print("----Liste des tables de la BDD SQLite3----")
print(list(cur))
print("----MEMBRES----")
print(list(car))

conn.commit()
cur.close()
car.close()
conn.close()


print("END OF EXEC")

os.system("pause")
