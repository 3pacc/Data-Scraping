import os
import mysql.connector
from bs4 import BeautifulSoup

# Répertoire contenant les fichiers HTML
repertoire = 'data'

def extract_data(fichier):
    with open(fichier, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        
        # Recherche du tableau de données
        tableau = soup.find('table', summary="Popularity for top 1000")
        lignes = tableau.find_all('tr')
        
        donnees = []
        for ligne in lignes[1:]:  # Ignorer la première ligne (en-tête)
            colonnes = ligne.find_all('td')
            
            # Vérifier si la ligne contient suffisamment de colonnes
            if len(colonnes) >= 3:
                rang = int(colonnes[0].get_text())
                nom_masculin = colonnes[1].get_text()
                nom_feminin = colonnes[2].get_text()
                donnees.append((rang, nom_masculin, nom_feminin))
        return donnees

def transform_and_load(data, fichier, user, password, database):
    conn = mysql.connector.connect(
        user=user,
        password=password,
        database=database
    )
    cursor = conn.cursor()
    
    # Création du nom de la table en utilisant l'année du fichier
    nom_table = f"Annee_{fichier[-9:-5]}"
    
    # Créer la table dans la base de données
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {nom_table} (
            rang INT,
            nom_masculin VARCHAR(255),
            nom_feminin VARCHAR(255)
        )
    ''')
    
    # Insérer les données extraites dans la table
    for donnee in data:
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
        
        # Transformation et chargement dans MySQL
        transform_and_load(data, chemin_fichier,'root', '', 'data_scraping')
