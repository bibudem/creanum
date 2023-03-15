# Wiki CréaNum

Wiki des espaces de création numérique des Bibliothèques UdeM. 
**Les travaux sont en cours et ceci n'est pas la version finale!**

Le wiki utilise un générateur de site statique Mkdocs avec le thème [Material for Mkdocs](https://github.com/squidfunk/mkdocs-material).

Le texte est rédigé avec Markdown et les images en WebP (conversion en local pour l'instant)

Note : La version Insiders est utilisée ici pour avoir plus de fonctionnalités. [En savoir plus](https://squidfunk.github.io/mkdocs-material/insiders/).

Pour copier le projet : 
``` sh
git clone https://github.com/bibudem/wiki.git
```

Idéalement, c'est de créer un environnement virtuel pour ne pas créer des conflits : 
``` sh
python3 -m venv venv
```

et l'activer :
``` sh
. venv/bin/activate 
```

Installer les dépendances avec pip : 
``` sh
pip install mkdocs-video mkdocs-glightbox mkdocs-table-reader-plugin
```

Si vous voulez lancer un aperçu en local, il faut désactiver certains plugins de la version *Insiders* dans le fichier mkdocs.insiders.yml :
``` yaml
# - blog
```

Certaines caractéristiques ne peuvent pas se générer en local sans la version Insiders, comme le *Card grids*, le *Anchor links*, *Navigation path*, etc. et peuvent être désactiver en les mettant en commentaires dans le fichier mkdocs.yml

À chaque *Push*, le site se génère automatiquement grâçe au *workflow* qui se trouve dans le dossier .github/workflows/ci.yml
et devient accessible sur Github Pages : [bibudem.github.io/wiki](https://bibudem.github.io/wiki)
