---

---

# Ultimaker

## Présentation de l'imprimante

[Ultimaker S3 ](https://www.notion.so/3d56a063be644e97ae4ae26c0dbb577b)

L’imprimante Ultimaker S3 est prête à l’emploi aussitôt sortie de sa boite. L’avantage de cette imprimante 3D est qu’elle ne nécessite pas de calibrage poussé : il n’est pas nécessaire de régler la hauteur de la première couche, contrairement à la [Prusa MK3S+](https://www.notion.so/Pr-sentation-de-l-imprimante-521d25a5fad74fb1bbbf7f5e717a5710). Tous ces réglages se font automatiquement par l’imprimante.

Le [bloc d’extrusion](https://www.notion.so/Extrudeur-t-te-d-impression-865ffec9ddf54b81ba4134e3d86f72d5) est monté sur deux axes (X et Y). Le plateau est monté sur l’axe Z. Le volume d’impression est protégé des quatre côtés, ce qui rend l’impression moins sensible aux courants d’air et aux changements de température soudains.

Le plateau d’impression est une vitre, ce qui donne un effet parfaitement lisse et brillant à la première couche des impressions.

Le bloc d’extrusion et doté de deux extrudeurs permettant d’imprimer facilement avec deux filaments différents.

Le *[feeder](https://www.notion.so/Nomenclature-de-l-impression-3D-ae1c1d1de83a4490b33ae8900346ebf1)* se trouve à l’arrière de l’imprimante et le filament passe par un tube pour être acheminé à l’extrudeur.  

Suivez les instructions à [cette page](https://www.notion.so/Proc-dure-de-changement-de-filament-3d05fd38103e4e07b83039256f1044c2) ****pour changer de filament.

<aside>
📌 Avant de lancer une première impression, vous devez lire [le guide de l'impression 3D](https://www.notion.so/Guide-de-l-impression-3D-2dfbdea9ff6f4e8082172534aca77ffb).

</aside>

<aside>
💡 Le logiciel est installé dans les postes informatiques des **Ateliers de fabrication numérique** avec la bonne configuration. Vous pouvez utiliser ces postes pour préparer votre fichier. Si vous préférez le faire avec votre ordinateur, suivez les instructions ci-dessous.

</aside>

## Logiciel de découpe Ultimaker Cura

Lien vers le téléchargement : [https://ultimaker.com/fr/software/ultimaker-cura](https://ultimaker.com/fr/software/ultimaker-cura)

Version utilisée dans ce tutoriel : 5.1.1

Compatible avec : Windows, Mac OS et Linux

<aside>
🚨 Le logiciel **n'est pas encore entièrement compatible** avec la puce M1 d'Apple. (nov 2021) [Consultez le support Ultimaker pour en savoir plus.](https://support.ultimaker.com/hc/en-us/articles/360018141480)

</aside>

## Instructions

1. Installez le logiciel **Ultimaker Cura**.
2. Au lancement du logiciel, cliquez sur **Get Started**.
3. Approuvez les conditions d’utilisation et cliquez sur **Next** dans la section Help us. 
4. Cliquez sur **Skip** dans la section Sign in. 
5. Dans Add a printer, cliquez sur **Add a non-networked printer** et sélectionnez **Ultimaker S3**. 
6. Dans What’s New, cliquez sur **Skip** et enfin dans Release Notes, cliquez sur **Finish**.

# **Première impression avec l’Ultimaker**

<aside>
📌 Avant de faire votre première impression, lisez le [Guide de l’impression 3D](https://www.notion.so/Guide-de-l-impression-3D-2dfbdea9ff6f4e8082172534aca77ffb) et [Installez le logiciel](https://www.notion.so/Configuration-Cura-495ec46b91744a1b98d8f17e3a98af74) Ultimaker Cura.

</aside>

Pour changer la langue de l’interface, cliquez sur **Préférences** > **Configurer Cura** et dans l’onglet **Général**, choisir la langue de votre choix. 

- À l’ouverture du logiciel de découpe Cura, il faut s’assurer qu’on a la bonne configuration. Assurez-vous que l’imprimante Ultimaker S3 est sélectionnée en haut à gauche de l’écran.

![Capture d’écran 2022-04-26 123139.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/44c344f5-efe3-48ad-a7d1-573adfc0c61a/Capture_dcran_2022-04-26_123139.png)

### Ajouter un modèle 3D au logiciel

Pour ajouter un modèle .STL, il existe plusieurs moyens : 

- Cliquez sur le bouton représentant un dossier en haut à gauche de l’écran (juste en dessous du logo).
- **File** > **Open File(s).**
- Raccourci clavier **CTRL-O** (ou **CMD-O** sur MacOS).
- Glisser-déposer le fichier sur le plateau.

### Navigation

- **Shift+clic** ou **clic sur la molette de la souris** = translation de caméra
- **Clic droit** = rotation de caméra
- **Rotation de la molette de la souris** = zoom/dézoome

### Échelle et taille

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0ab91e55-2b72-4fe7-9901-cd690e6175ef/Untitled.png)

Permet de déplacer les objets sur le plateau d’impression.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/37354a0a-7385-44ed-a224-fc075c361792/Untitled.png)

Permet de modifier l’échelle du modèle selon un axe précis ou dans son entièreté.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7d62b93d-1eec-43d5-b72e-3778cab18a53/Untitled.png)

Permet d’effectuer une rotation du modèle.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c0978560-001e-43f3-8413-403b6ecf85d7/Untitled.png)

Permet de permuter le modèle de manière symétrique (effet miroir).

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/99b14798-c785-43c0-b971-9dcfe5b34d1d/Untitled.png)

Permet l’utilisation de paramètres avancés.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/321d2193-d26d-4596-afff-b7475af418fe/Untitled.png)

Permet de générer manuellement des zones sans support.

### Réglages

![ultimaker.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c1a73287-c6f2-4b97-beb5-fe1e82cfc02c/ultimaker.png)

1. **Imprimante** : Assurez-vous que le bon modèle est sélectionné. Dans les ateliers de l’Université de Montréal, on retrouve généralement des Ultimaker S3. ([voir la liste des équipements par bibliothèque ici](https://www.notion.so/fada784ac8a648128846afe7c75818cc)). 
2. **Filament** (extrudeur 1) : Sélectionnez **Generic PLA***.* Cette configuration contient les valeurs de température de l’extrudeur et du plateau (par défaut : 215°C pour l’extrudeur, 60°C pour le plateau).
3. **Filament** (extrudeur 2) : Selon si vous souhaitez imprimer une deuxième couleur ou des supports, sélectionnez **Generic PLA.** Si vous utilisez du **PVA**, il faut changer la tête d’extrusion à **BB**.
4. **Réglages d’impression** : Sélectionnez la hauteur de la couche : 0.10 mm pour une impression de précision, 0.20 mm pour une impression normale et 0.30 mm pour des tests ou des pièces qui n’ont pas besoin d’être de qualité.
5. **Remplissage** : Indiquez le pourcentage de remplissage. Il n’est pas nécessaire de faire un remplissage au-delà de 30%.
6. **Supports** : Si une partie de votre modèle commence dans les airs et n'est supportée par aucun élément en dessous, vous devez ajouter une structure de support pour réussir une impression. Plusieurs options s’offrent à vous. Si votre modèle n’a pas besoin de support, laissez décoché. Si un support est nécessaire, cochez l’option et sélectionnez **Extruder 1** ou **Extruder 2** selon le filament que vous voulez utiliser pour les supports.
7. **Adhérence** : en l’activant, on crée une bordure qui augmente la surface d’adhésion de la première couche afin d’augmenter l’adhérence au plateau.

<aside>
💡 Le plateau de l’Ultimaker est très adhérent, il n’est généralement pas nécessaire d’ajouter l’option de bordure.

</aside>

### Découpage

Pour découper le modèle, cliquer sur **Découper** en bas à droite de la fenêtre.

L’option **Aperçu** permet de vérifier le déroulement de l’impression.

Les couleurs illustrées identifient les différentes parties du modèle (coque, remplissage, jupe, support).

### Préparation de l’imprimante

Avant de lancer l’impression ou de changer le filament, vous devez nettoyer le plateau.

Pour l’Ultimaker, il faut imbiber une lingette de nettoyant à vitres et nettoyer le plateau avec.

Si vous voulez changer de filament, [suivez la procédure de changement de filament](https://www.notion.so/Proc-dure-de-changement-de-filament-3d05fd38103e4e07b83039256f1044c2).

### Lancement de l’impression

- Introduire la clé USB au devant de l’imprimante.
- L’imprimante chargera les fichiers. Naviguez vers le nom de votre fichier et appuyez sur le bouton.
- Il est important de surveiller les premières couches de l’impression afin de s’assurer que le modèle adhère au plateau.

## Pour en savoir plus

[Ultimaker Cura](https://support.ultimaker.com/hc/en-us/sections/360003548339-Ultimaker-Cura)

[Blog sur l'impression 3D | Ultimaker](https://ultimaker.com/fr/learn/blog)

Sauf indications contraires, les contenus de ce wiki créé par les [Bibliothèques UdeM](http://bib.umontreal.ca) sont sous [licence CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

![https://i.creativecommons.org/l/by/4.0/88x31.png](https://i.creativecommons.org/l/by/4.0/88x31.png)

[Nous joindre](https://www.notion.so/Nous-joindre-33f9bd7c0c67457da83396c179ccb487)

![Bleu-UdeM_monde-RGB.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/bc389c51-3dde-442e-8e16-7c65c58b4505/Bleu-UdeM_monde-RGB.png)

# Procédure de changement de filament

---

<aside>
💡 Diamètre des filaments de l'Ultimaker S3 : **2.85mm**

</aside>

Accédez au menu de l’icône imprimante, ensuite, cliquez sur **PLA**.

![https://i.imgur.com/7VfL7kR.jpg](https://i.imgur.com/7VfL7kR.jpg)

![https://i.imgur.com/XpNaRsD.jpg](https://i.imgur.com/XpNaRsD.jpg)

Choisissez **Modifier** s’il y a une bobine déjà installée, ou **Insérer** s’il n’y a aucune bobine.

![https://i.imgur.com/hRFwQmg.jpg](https://i.imgur.com/hRFwQmg.jpg)

La buse se chauffe afin d’atteindre la température de fusion et extraire facilement le filament. Soyez prêt à guider la sortie du filament et de le faire suivre sur la bobine pour éviter la formation de nœuds.

![https://i.imgur.com/G3ZaVlD.jpg](https://i.imgur.com/G3ZaVlD.jpg)

Si, en tirant délicatement le filament, ça reste coincé, soulevez la languette afin de le faire libérer du mécanisme du *feeder*. N'oubliez pas de remettre la languette à sa place par la suite.

![https://i.imgur.com/xRQXMsd.jpg](https://i.imgur.com/xRQXMsd.jpg)

![https://i.imgur.com/R1dVh0t.jpg](https://i.imgur.com/R1dVh0t.jpg)

Installez la nouvelle bobine de 2.85mm, l’extrémité du filament doit venir d’en bas. Mettez le bout du filament dans le trou prévu à cet effet et poussez légèrement. L’imprimante va détecter le filament et le tirer **très lentement** vers le tube. Si l’imprimante ne détecte pas le filament, levez la languette vers le haut et poussez le filament jusqu’à ce que vous le voyiez au début du tube.

![https://i.imgur.com/s6DrjRc.jpg](https://i.imgur.com/s6DrjRc.jpg)

Confirmez dans l’écran que le filament est en place.

![https://i.imgur.com/4XTzcvC.jpg](https://i.imgur.com/4XTzcvC.jpg)

![https://i.imgur.com/G9thYzg.jpg](https://i.imgur.com/G9thYzg.jpg)

Indiquez quel type de matériel a été mis (dans notre cas, du PLA).

<aside>
💡 Si vous avez installé une bobine de la marque Ultimaker, cette dernière est équipée d'une puce NFC. L'imprimante détectera automatiquement le type de filament.

</aside>

![https://i.imgur.com/LwhVZGE.jpg](https://i.imgur.com/LwhVZGE.jpg)

![https://i.imgur.com/G93J6SD.jpg](https://i.imgur.com/G93J6SD.jpg)

L’imprimante va tirer le filament jusqu’à l’extrudeur et commencer à faire une purge de la couleur précédente. Une fois que la couleur change, confirmez sur l’écran.

![https://i.imgur.com/PgMAJAb.jpg](https://i.imgur.com/PgMAJAb.jpg)

![https://i.imgur.com/lUtsJvc.jpg](https://i.imgur.com/lUtsJvc.jpg)

![https://i.imgur.com/NGvvFFG.jpg](https://i.imgur.com/NGvvFFG.jpg)

## Ressources

[Loading materials on the Ultimaker S5](https://support.ultimaker.com/hc/en-us/articles/360011427140)

[Change the Ultimaker S5 configuration](https://support.ultimaker.com/hc/en-us/articles/360011544619-Change-the-Ultimaker-S5-configuration)

Sauf indications contraires, les contenus de ce wiki créé par les [Bibliothèques UdeM](http://bib.umontreal.ca) sont sous [licence CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

![https://i.creativecommons.org/l/by/4.0/88x31.png](https://i.creativecommons.org/l/by/4.0/88x31.png)

[Nous joindre](https://www.notion.so/Nous-joindre-33f9bd7c0c67457da83396c179ccb487)

![Bleu-UdeM_monde-RGB.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/bc389c51-3dde-442e-8e16-7c65c58b4505/Bleu-UdeM_monde-RGB.png)