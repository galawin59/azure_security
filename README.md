# azure_security
 
Mise en place d'un script python permettant de transferer un fichier csv depuis un site web sur le container d'un datalake Azure 
en respectant les regles de sécurité du moindre privilege et les roles

Le script recupere le secret du service principale en etant connecté au service secondaire pour pouvoir se connecter au service principale
et ensuite transferer le fichier.


# Azure Databricks

Etape de configuration :

Creer un acces policies en get/list sur le secret permission pour le databricks sur le keyvault qui contient la clef secret du service principal

Pour le code de recuperation du fichier 

"abfss://airbnb@datalakepb.dfs.core.windows.net/listings.csv"

adbfss = connection au storage
airbnb = nom du contenaire
datalakepb = non du datalake
listings.csv = nom du fichier a recuperer

