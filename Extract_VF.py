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

