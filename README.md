# Programme d'extraction, transformation et chargement (ETL) de données HTML vers une base de données MySQL

Ce programme extrait des données à partir de fichiers HTML, les transforme et les charge dans une base de données MySQL.

## Configuration requise

- Python 3
- Le module `mysql-connector-python` (pour la connexion à la base de données MySQL)
- Le module `beautifulsoup4` (pour l'analyse HTML)

## Utilisation

1. Assurez-vous d'installer les modules requis en utilisant `pip install mysql-connector-python beautifulsoup4` si ce n'est pas déjà fait.

2. Placez vos fichiers HTML dans le répertoire `data`.

3. Modifiez les informations de connexion à la base de données MySQL dans le fichier `main.py`.

4. Exécutez le programme en utilisant la commande suivante :

   ```bash
   python main.py

-Les données seront extraites, transformées et chargées dans des tables distinctes de la base de données MySQL.

## Structure du programme

Le programme est divisé en trois étapes principales :

1- Extraction : Les données sont extraites à partir des fichiers HTML en utilisant BeautifulSoup.

2- Transformation : Les données sont transformées en tables distinctes basées sur l'année du fichier.

3- Chargement : Les données transformées sont chargées dans une base de données MySQL.
