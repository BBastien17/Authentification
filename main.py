#Importation des librairies
#Il faudra aussi installer sqlite au préalable et db browser for sqlite
import sqlite3 as sq

#On crée une variable qui va se connecter à notre base de données
conn=sq.connect("Auth_DB.dbs")
#A l'exécution la base de données est créée

#On va ensuite exécuter différentes requêtes SQL
#On commence par créer une variable pour le curseur qu'on exécute ensuite
c=conn.cursor()
#On définit les différentes informations de notre table avec une clé primaire qui s'incrémente automatiquement
c.execute("""create table if not exists Auth_DB 
(id integer primary key autoincrement, nom text, prenom text, email text)""")
#La commande dans les guillemets permet de ne pas écraser la table si elle existe déjà
#Commande pour insérer un attribut dans lequel nous devrons donner un exemple de nom prénom...
c.execute("""insert into Auth_DB (nom,prenom,email) values ("BOYER","Bastien","bastien@gmail.com") """)
#On affiche les données que l'on a dans la table sql avec un select
c.execute("""select * from Auth_DB""")
#Affichage de la première ligne de notre DB
print(c.fetchone())
#On peut aussi parcourir toutes les données de notre DB à l'aide d'une fonction
items=c.fetchall()
for item in items:
    print(item)
#On envoie ensuite l'insertion réalisée pour qu'elle soit prise en compte
conn.commit()

#On ferme ensuite la base de données
conn.close()


