import os
import mysql.connector
from Extract_VF import repertoire, extract_data
from Transform_VF import transform



def load(data, user, password, database):
    conn = mysql.connector.connect(
        user=user,
        password=password,
        database=database
    )
    cursor = conn.cursor()
    
    for nom_table, donnees in data.items():
        # Créer la table dans la base de données
        cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {nom_table} (
                rang INT,
                nom_masculin VARCHAR(255),
                nom_feminin VARCHAR(255)
            )
        ''')
        
        # Insérer les données extraites dans la table
        for donnee in donnees:
            cursor.execute(f'''
                INSERT INTO {nom_table} (rang, nom_masculin, nom_feminin)
                VALUES (%s, %s, %s)
            ''', donnee)
    
    # Valider et fermer la base de données
    conn.commit()
    conn.close()

# Parcourir les fichiers HTML dans le répertoire
for fichier in os.listdir(repertoire):
    if fichier.endswith('.html'):
        chemin_fichier = os.path.join(repertoire, fichier)
        
        # Extraction des données
        data = extract_data(chemin_fichier)
        
        # Transformation des données
        data_transformed = transform(data, chemin_fichier)
        
        # Chargement dans MySQL
        load(data_transformed, 'root', '','data_scraping')
