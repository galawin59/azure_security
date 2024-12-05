# azure_security
 
Mise en place d'un script python permettant de transferer un fichier csv depuis un site web sur le container d'un datalake Azure 
en respectant les regles de sécurité du moindre privilege et les roles

Le script recupere le secret du service principale en etant connecté au service secondaire pour pouvoir se connecter au service principale
et ensuite transferer le fichier.

On met dans un .env le client_id, le tenant_id et le secret du service secondaire qui n'a que les droits de lire le secret du service principle qui est dans le key vault
ensuite cela nous permet de nous connecter au service principale pour effectuer le transfere de fichier ;) 


# Azure Databricks

Etape de configuration :

Creer un acces policies en get/list sur le secret permission pour le databricks sur le keyvault qui contient la clef secret du service principal

Pour le code de recuperation du fichier 

"abfss://airbnb@datalakepb.dfs.core.windows.net/listings.csv"

adbfss = connection au storage </br>
airbnb = nom du contenaire </br>
datalakepb = non du datalake </br>
listings.csv = nom du fichier a recuperer

