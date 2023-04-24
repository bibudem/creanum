import os
import re
from PIL import Image

# Définir le répertoire racine pour la recherche d'images
root_dir = 'docs/assets/images'

# Convertir tous les fichiers jpeg, jpg et png en webp
for root, dirs, files in os.walk(root_dir):
    for filename in files:
        if filename.endswith('.jpeg') or filename.endswith('.jpg') or filename.endswith('.png'):
            src_path = os.path.join(root, filename)
            file_name = os.path.splitext(filename)[0] # obtenir le nom de fichier sans l'extension
            dest_path = os.path.join(root, file_name + '.webp') # utiliser le nom de fichier sans extension pour créer le nouveau nom de fichier en ajoutant ".webp"
            try:
                img = Image.open(src_path)
                img = img.convert('RGB')
                img.save(dest_path, 'webp', quality=40)
                os.remove(src_path)
                print(f'{src_path} converti en {dest_path}')
            except (IOError, FileNotFoundError) as e:
                print(f'Erreur lors de la conversion de {src_path} : {e}')

# Parcourir tous les fichiers html dans le répertoire courant
for root, dirs, files in os.walk('docs'):
    for filename in files:
        if filename.endswith('.html'):
            filepath = os.path.join(root, filename)
            try:
                with open(filepath, 'r') as file:
                    # Lire le contenu du fichier html
                    content = file.read()

                    # Remplacer tous les liens avec les extensions jpeg, jpg et png par webp
                    content = re.sub(r'(\.jpeg|\.jpg|\.png)', r'.webp', content)

                # Écrire le contenu mis à jour dans le fichier html
                with open(filepath, 'w') as file:
                    file.write(content)
                    print(f'{filepath} mis à jour avec les liens webp')
            except (IOError, FileNotFoundError) as e:
                print(f'Erreur lors de la mise à jour de {filepath} : {e}')

# Parcourir tous les fichiers markdown dans le répertoire courant
for root, dirs, files in os.walk('docs'):
    for filename in files:
        if filename.endswith('.md') or filename.endswith('.markdown'):
            filepath = os.path.join(root, filename)
            try:
                with open(filepath, 'r') as file:
                    # Lire le contenu du fichier markdown
                    content = file.read()

                    # Remplacer tous les liens avec les extensions jpeg, jpg et png par webp
                    content = re.sub(r'(\.jpeg|\.jpg|\.png)', r'.webp', content)

                # Écrire le contenu mis à jour dans le fichier markdown
                with open(filepath, 'w') as file:
                    file.write(content)
                    print(f'{filepath} mis à jour avec les liens webp')
            except (IOError, FileNotFoundError) as e:
                print(f'Erreur lors de la mise à jour de {filepath} : {e}')

# Supprimer tous les fichiers jpeg, jpg et png d'origine
for root, dirs, files in os.walk(root_dir):
    for filename in files:
        if filename.endswith('.jpeg') or filename.endswith('.jpg') or filename.endswith('.png'):
            filepath = os.path.join(root, filename)
            try:
                os.remove(filepath)
                print(f'{filepath} supprimé')
            except (IOError, FileNotFoundError) as e:
                print(f'Erreur lors de la suppression de {filepath} : {e}')