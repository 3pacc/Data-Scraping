def transform(data, fichier):
    # Création du nom de la table en utilisant l'année du fichier
    nom_table = f"Annee_{fichier[-9:-5]}"
    
    tables = {}
    for donnee in data:
        if nom_table not in tables:
            tables[nom_table] = []
        tables[nom_table].append(donnee)
    return tables


