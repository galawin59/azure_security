from azure.identity import DefaultAzureCredential,ClientSecretCredential
from azure.storage.blob import BlobServiceClient
from azure.keyvault.secrets import SecretClient
from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup

load_dotenv()


#connection au sp secondaire pour recuperer le secret pour se connecter au service principale
defaut_credential = ClientSecretCredential(
       tenant_id=os.getenv('tenant_id'),
       client_id=os.getenv('client_id'),
       client_secret=os.getenv('secret_id'),
   )
#recuperation de la clef
secret_client = SecretClient("https://keyvaultpatrbaudry.vault.azure.net", credential =  defaut_credential)
secret = secret_client.get_secret("secretspone")

""" print(secret.name)
print(secret.value) """
#connection au service principal
service_credential = ClientSecretCredential(
       tenant_id=os.getenv('tenant_id_sp'),
       client_id=os.getenv('client_id_sp'),
       client_secret=secret.value,
)


""" print(service_credential._client_credential) """

#connection au datalake avec le service principal
blob_service_client = BlobServiceClient(
    account_url="https://datalakepb.blob.core.windows.net",
    credential=service_credential
)

#connection au site pour recuperer le csv
container_name = "airbnb"
blob_name = "listings.csv"
url = "https://data.insideairbnb.com/spain/catalonia/barcelona/2024-09-06/visualisations/listings.csv"

response = requests.get(url)
if response.status_code == 200:
    # Créer un client pour le conteneur
    container_client = blob_service_client.get_container_client(container_name)

    # Créer un client pour le blob
    blob_client = container_client.get_blob_client(blob_name)

    # Télécharger le fichier dans le conteneur
    blob_client.upload_blob(response.content, overwrite=True)

    print(f"Fichier téléchargé avec succès depuis {url} dans le conteneur {container_name} sous le nom {blob_name}.")
else:
    print(f"Échec du téléchargement du fichier depuis {url}. Statut : {response.status_code}")


""" credential = ClientSecretCredential(
       tenant_id=os.getenv('tenant_id'),
       client_id=os.getenv('client_id'),
       client_secret=secret.value,
   )
 """

""" afficher liste secret """
""" secret_properties = secret_client.list_properties_of_secrets()

for secret_property in secret_properties:
    # the list doesn't include values or versions of the secrets
    print(secret_property.name) """


""" supprimer des secret """

""" deleted_secret = secret_client.begin_delete_secret("test").result()

print(deleted_secret.name)
print(deleted_secret.deleted_date) """