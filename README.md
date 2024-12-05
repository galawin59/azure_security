# azure_security
 
Mise en place d'un script python permettant de transferer un fichier csv depuis un site web sur le container d'un datalake Azure 
en respectant les regles de sécurité du moindre privilege et les roles

Le script recupere le secret du service principale en etant connecté au service secondaire pour pouvoir se connecter au service principale
et ensuite transferer le fichier.
