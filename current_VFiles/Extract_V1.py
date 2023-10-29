from bs4 import BeautifulSoup
import mysql.connector

# Liste des noms de fichiers HTML à traiter
noms_fichiers = [
    "data/baby1990.html", "data/baby1992.html", "data/baby1994.html",
    "data/baby1996.html", "data/baby1998.html", "data/baby2000.html",
    "data/baby2002.html", "data/baby2004.html", "data/baby2006.html",
    "data/baby2008.html"
]

# Créez une liste pour stocker les données de tous les fichiers
donnees_totales = []

# Connectez-vous à la base de données MySQL
conn = mysql.connector.connect(
    user="root",
    password="",
    database="data_scraping"
)
cursor = conn.cursor()

# Boucle à travers les fichiers
for nom_fichier in noms_fichiers:
    chemin_fichier = "data/" + nom_fichier

    # Ouvrez le fichier HTML
    with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
        # Utilisez Beautiful Soup pour analyser le contenu HTML
        soup = BeautifulSoup(fichier, 'html.parser')

        # Trouvez le tableau contenant les données
        tableau = soup.find('table', summary="formatting")

        # Créez une liste pour stocker les données de ce fichier
        donnees_fichier = []

        # Parcourez les lignes du tableau et extrayez les données
        lignes = tableau.find_all('tr')[1:]  # Ignorez la première ligne d'en-tête
        for ligne in lignes:
            colonnes = ligne.find_all('td')

            # Assurez-vous que la ligne a suffisamment de colonnes
            if len(colonnes) == 3:
                rank = colonnes[0].get_text()
                nom_masculin = colonnes[1].get_text()
                nom_feminin = colonnes[2].get_text()

                # Stockez les données dans un dictionnaire
                entree = {
                    "Rank": rank,
                    "Nom masculin": nom_masculin,
                    "Nom féminin": nom_feminin
                }
                donnees_fichier.append(entree)

                # Insérez les données dans la base de données MySQL
                insert_query = "INSERT INTO Data_files (Rank, NomMasculin, NomFeminin) VALUES (%s, %s, %s)"
                insert_values = (rank, nom_masculin, nom_feminin)
                cursor.execute(insert_query, insert_values)
                conn.commit()

        # Ajoutez les données de ce fichier à la liste totale
        donnees_totales.append(donnees_fichier)

# Fermez la connexion à la base de données MySQL
cursor.close()
conn.close()
