# -*-coding:Latin-1 -*
import os
import sqlite3
import unittest
import logging

fichierDonnees ="bd_test.sq3"
conn =sqlite3.connect(fichierDonnees)
conn.text_factory = str
cur =conn.cursor()
car =conn.cursor()
cir =conn.cursor()

# cur.execute("CREATE TABLE membres (age INTEGER, nom TEXT, taille REAL)")
# cur.execute("INSERT INTO membres(age,nom,taille) VALUES(21,'Dupont',1.83)")
# cur.execute("INSERT INTO membres(age,nom,taille) VALUES(15,'Blumar',1.57)")
# cur.execute("INSERT Into membres(age,nom,taille) VALUES(18,'Ozemir',1.69)")

# cur.execute("DELETE FROM membres where age >1")

class TestFonction(unittest.TestCase):
    # Chaque méthode dont le nom commence par 'test_'
    # est un test1.

 def setUp(self):
  conn =sqlite3.connect(fichierDonnees)
  cur =conn.cursor()
  car =conn.cursor()
  cir =conn.cursor()
  print("SetUp")


 def tearDown(self):
  #conn.commit()
  #cur.close()
  #car.close()
  #cir.close()
  conn.close()
  print(" ")
  print("TearDown")
  os.system("pause")

 def test_get_element(self):

  cir.execute("Select age from membres where nom='Dupont'")
  first=cir.fetchone()[0]
  self.assertEqual(first,10)

 def test_get_element2(self):
  conn =sqlite3.connect(fichierDonnees)
  cir =conn.cursor()
  cir.execute("Select age from membres where nom='Blumar'")
  first=cir.fetchone()[0]
  self.assertEqual(first,15)



cur.execute("select name from sqlite_master where type = 'table'")
print("----Liste des tables de la BDD SQLite3----")
print(list(cur))
car.execute("select * from membres")
print("----MEMBRES----")
print(list(car))

if __name__ == '__main__':
    unittest.main()
    print("THE END")
    os.system("pause")
