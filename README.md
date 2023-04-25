# Wiki CréaNum
## Wiki des espaces de création numérique des Bibliothèques UdeM. 
**WORK IN PROGRESS**

Le wiki utilise un générateur de site statique Mkdocs avec le thème [Material for Mkdocs](https://github.com/squidfunk/mkdocs-material). Le texte est rédigé en Markdown et les images en WebP. La version *Insiders* est utilisée ici pour avoir plus de fonctionnalités. [En savoir plus](https://squidfunk.github.io/mkdocs-material/insiders/).

## Installation 

Pour cloner le projet : 
``` sh
git clone https://github.com/bibudem/creanum.git
```

Idéalement, c'est de créer un environnement virtuel : 
``` sh
python3 -m venv venv
```

et l'activer :
``` sh
. venv/bin/activate 
```

Installer les paquets requis avec pip : 
``` sh
pip install -r requirements.txt
```

et enfin Material for Mkdocs :
``` sh
pip install mkdocs-material
```

## Aperçu local

Si vous voulez lancer un aperçu en local, il faut désactiver certains plugins de la version *Insiders* dans les fichiers de configuration. Certaines caractéristiques ne peuvent pas se générer en local sans la version *Insiders*, comme le *Card grids*, le *Anchor links*, *Navigation path*, etc. et peuvent être désactiver en les mettant en commentaires dans le fichier mkdocs.yml et mkdocs.insiders.yml :

``` yaml
# - blog
```

Pour lancer un aperçu en local : 
``` sh
mkdocs serve --config-file mkdocs.insiders.yml
```

## Note
### Github Pages
À chaque *Push*, le site se génère automatiquement grâce au *workflow* qui se trouve dans le dossier .github/workflows/ci.yml
et devient accessible sur Github Pages : [bibudem.github.io/creanum](https://bibudem.github.io/creanum). Le GH_TOKEN est configuré pour générer le site avec la version *Insiders* automatiquement. 

### Conversion des images en WebP
le script webp.py permet de convertir automatiquement en WebP les images qui se trouvent dans le dossier docs/assets/images et ceci à chaque déploiement. Il cherche par la suite toutes mentions de .jpg, .jpeg ou .png dans les fichiers .md et .html et les remplace par .webp. Magique. 
La conversion vers ce format se fait avec le paquet Pillow.

