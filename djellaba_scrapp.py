import requests
from bs4 import BeautifulSoup
import os

# Définir l'URL de la page web à scrapper
url = "https://ma.diamantine.com/categorie/femme/tradition/djellaba/page/5/"

# Récupérer le contenu HTML de la page
response = requests.get(url)

# Analyser le contenu HTML avec BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Créer un dossier "images" pour enregistrer les images
if not os.path.exists("images_Djellaba"):
    os.mkdir("images_Djellaba")

# Trouver toutes les balises "img" dans le contenu HTML de la page
img_tags = soup.find_all('img')

# Télécharger et enregistrer chaque image dans le dossier "images"
for img in img_tags:
    img_url = img.get('src')
    if img_url:
        try:
            # Récupérer le contenu binaire de l'image
            img_response = requests.get(img_url)

            # Enregistrer l'image dans un fichier dans le dossier "images"
            with open(os.path.join("images_Djellaba", os.path.basename(img_url)), "wb") as f:
                f.write(img_response.content)
        except:
            print("Impossible de télécharger l'image à l'URL:", img_url)