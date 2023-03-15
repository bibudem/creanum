# Prusa i3 Mk3s+

!!! note "Votre contribution est la bienvenue!"
    Cette page est en constante évolution. Si vous aussi vous voulez contribuer à son amélioration, consultez "[Comment contribuer?](https://www.notion.so/Comment-contribuer-2a3ad7b814524991b288cf91012f1f10)"

!!! info "Important"
    Avant de faire votre première impression, lisez l'[introduction à l'impression 3D](introduction.md)

## Présentation de l'imprimante

![Prusa i3 Mk3s+ à la Bibliothèque des sciences](../../assets/images/prusa-photo.webp)

| Prusa i3 Mk3s+||
|-----|-----|
|Volume d'impression|	25×21×21cm (9.84"×8.3"×8.3")|
|Buses disponibles|	0.4mm|
|Hauteur des couches|	0.05 - 0.35 mm|
|Diamètre du filament|	1.75 mm|
|Matériaux supportés|	PLA, PETG, ASA, ABS, PC, CPE, PVA/BVOH, PVB, HIPS, PP, Flex, nGen, Nylon, Carbon filled, Woodfill and other filled materials.|
|Surface d'impression|	Removable magnetic steel sheets(*) with different surface finishes|
|Impression multi-filament|	Possible en modifiant le gcode, ou en ajoutant le module MMU2S|
|Logiciel de découpe (slicer)|	PrusaSlicer|

Chaque imprimante a été montée par l'équipe. Toutes les parties en plastique ont été fabriquées par des imprimantes 3D, de sorte que ces pièces peuvent facilement être remplacées. Ce principe est appelé RepRap. 

Le bloc d’extrusion est monté sur deux axes (X et Z), le plateau est monté sur l’axe Y.
Le plateau d’impression est une feuille magnétique texturée. La première couche de l’impression aura une texture granuleuse.

Le *feeder* se trouve directement sur le dessus du bloc d’extrusion.

!!! info Ressources en ligne
    [Original Prusa i3 MK3S+ | Original Prusa 3D printers directly from Josef Prusa](https://www.prusa3d.com/fr/categorie/original-prusa-i3-mk3s/)

### Localisation

| Bibliothèque | Nombre |
|---|---|
|Sciences | 2 |
|Mathématiques et informatique | 1 |
|Thérèse-Gouin-Décarie| 1 |

## **Changement de filament**

!!! Warning " "
    Diamètre des filaments de la Prusa i3 MK3S+ : **1.75mm**

### **Retrait d’une bobine**

1. Dans le menu de la Prusa, sélectionnez **Unload filament**.
    
![Menu de la Prusa](../../assets/images/prusa-filament-1.webp)
    
2. Sélectionnez **PLA 215/60**. La buse va se chauffer afin que le filament se retire facilement.
    
![Menu de la Prusa](../../assets/images/prusa-filament-2.webp)
    
3. Au signal sonore, appuyez sur le bouton du menu, puis **tirez délicatement** le filament vers le haut.
4. Coupez le bout du filament avec une pince coupante en angle, mettre dans le bout dans un des trous de la bobine et ranger la bobine dans un sac hermétique. Suivez les consignes pour l’entreposage des filaments.

### **Installer une nouvelle bobine**

1. Coupez le bout du filament de la nouvelle bobine avec une pince coupante en angle.
2. Installez la nouvelle bobine sur le support tout en veillant à ce que le bout passe d’en haut.
3. La fonction **Autoload filament** est activée par défaut, l’imprimante détectera automatiquement s’il y a présence d’un filament. Mettez le filament dans le trou sans forcer, vous allez sentir le filament tirer vers le bas doucement. L’écran indiquera **Loading filament** (chargement du filament).
    
![Menu de la Prusa](../../assets/images/prusa-filament-3.webp)
    
4. Au bout de quelques secondes, vous devriez voir apparaitre la couleur précédente sortir de l’extrudeur, suivie de la nouvelle couleur. L’imprimante vous demandera si le filament est extrudé et avec la bonne couleur (*Filament extruding & with correct color?*). Confirmez en sélectionnant **Yes**, sinon, sélectionnez **No**, l’imprimante continuera à extruder jusqu’à l’apparition du filament.
    
![Menu de la Prusa](../../assets/images/prusa-filament-4.webp)
![Menu de la Prusa](../../assets/images/prusa-filament-5.webp)

!!! Warning "Attention"
    En aucun cas, vous ne devriez forcer, au risque d’endommager l’imprimante. Dans le doute, demandez de l’aide.

!!! Info "Ressources en ligne"
    [Prusa Printer: Changing Filament](https://youtu.be/12bYIGgkqIQ)

## Configuration PrusaSlicer

💡 Le logiciel est installé dans les postes informatiques des **Ateliers de fabrication numérique** avec la bonne configuration. Vous pouvez utiliser ces postes pour préparer votre fichier. Si vous préférez le faire avec votre ordinateur personnel, suivez les instructions ci-dessous.

### Logiciel de découpe PrusaSlicer

Lien vers le téléchargement : [https://www.prusa3d.com/page/prusaslicer_424](https://www.prusa3d.com/page/prusaslicer_424/)
Version utilisée dans ce tutoriel : **2.5**
Compatible avec : Windows, Mac OS, Linux.

### Assistant configuration

- Installez le logiciel PrusaSlicer sur votre machine.
- Au démarrage du logiciel, un assistant de configuration s’affichera, cliquez sur suivant.
- À l’étape Prusa FFF, décochez **0.4 mm buse** au dessous de **Original Prusa Mini & Mini+** et ****cochez **0.4 mm buse** au dessous de **Original Prusa i3 MK3s & MK3s+.**
- Cliquez sur **Fin**.

![Assistant configuration PrusaSlicer](../../assets/images/prusa-installation.webp)

## Première impression

À l’ouverture du logiciel de découpe PrusaSlicer, il faut s’assurer qu’on a la bonne configuration. Il doit y avoir une inscription sur le plateau mentionnant le modèle de l’appareil (**ORIGINAL PRUSA i3 MK3**). Si ce n’est pas le cas, changez le modèle de l’imprimante dans **Imprimante** (ou **Printer***)* à droite de l’écran (au dessous de **Filament**)

![Interface du logiciel PrusaSlicer](../../assets/images/prusa-impression-1.webp)

### Ajouter un modèle 3D

![Interface du logiciel PrusaSlicer](../../assets/images/prusa-impression-2.webp)

Pour ajouter un modèle .STL, cliquez sur le bouton **Add** (cube avec le bouton + en haut), ou allez dans **File > Import > Import STL/OBJ/AMF/3MF***...* ou encore avec le raccourci clavier ++ctrl+i++ (ou ++"cmd"+i++ pour MacOS).

### Navigation

Utilisez la souris ainsi que la molette pour tourner autour de l’objet et zoomer.

Clic gauche = rotation du plateau

Clic droit = translation de la caméra

![video](../../assets/videos/prusa-navigation.mp4)

### Échelle et taille

![video](../../assets/videos/prusa-dimension.mp4)

Redimensionnez la pièce en utilisant la fonction **Redimensionner** (menu de droite). Vous pouvez aussi changer les valeurs de l’échelle et de la taille à droite de l’écran. 

### Réglages

![Interface du logiciel PrusaSlicer](../../assets/images/prusa-impression-3.webp)

- **Réglages d’impression** : Sélectionnez la hauteur de la couche. 0.10mm pour une impression de précision, 0,20mm pour une impression normale et 0,30mm pour des tests ou des pièces qui n’ont pas besoin d’être de qualité.
- **Filament** : Sélectionnez **Generic PLA***.* Cette configuration contient les valeurs de température de l’extrudeur et du plateau (par défaut : 215c pour l’extrudeur, 60c pour le plateau).
- **Imprimante** : Assurez-vous que le bon modèle est sélectionné.
- **Supports** : Si une partie de votre modèle commence dans les airs et n'est supportée par aucun élément en dessous, vous devez ajouter une structure de support pour réussir une impression. Plusieurs options s’offrent à vous. Si votre modèle n’a pas besoin de support, sélectionnez **Aucun**. Si un support est nécessaire, sélectionnez **Support sur le plateau uniquement**, qui va créer des supports qui ont leur base au niveau du plateau.
- **Remplissage** : Indiquez le pourcentage de remplissage. Il n’est pas nécessaire de faire un remplissage au-delà de 30%.
- **Bordure** : en l’activant, on augmente le surface d’adhésion de la première couche afin d’augmenter l’adhérence au plateau.

### Découpage

Cliquez sur **Découper maintenant** (en anglais : **Slice now**, **CTRL-R** sur Windows et Linux, **CMD-R** sur MacOS). 

![Interface du logiciel PrusaSlicer](../../assets/images/prusa-impression-4.webp)

Le logiciel passe en mode aperçu. Vous pouvez basculer entre ce mode et celui de Vue d’éditeur 3D en appuyant sur la touche **Tab**.

Vous pouvez visualiser couche par couche votre impression ainsi que le déplacement de la tête d’impression.

![video](../../assets/videos/prusa-couche.mp4)

Si jamais vous changez un réglage, la pièce disparait de l’écran. Vous devez soit revenir à la vue d’édition 3D ou découper la pièce à nouveau. 

Si vous êtes satisfait de l’aperçu, appuyez sur **Exporter le G-code** en bas à droite et déplacez le fichier dans la carte SD. Si la carte SD est déjà insérée dans votre ordinateur, appuyez sur le bouton à côté représentant une clé USB et une carte SD.

### Préparation de l’imprimante

Avant de lancer l’impression ou de changer le filament, vous devez nettoyer le plateau.
Pour la Prusa, il faut imbiber une lingette de nettoyant à vitres et nettoyer le plateau avec, en évitant de faire bouger le plateau.  

Si vous voulez changer de filament, [suivez la procédure de changement de filament](https://www.notion.so/Proc-dure-de-changement-de-filament-17802010bb994b74ae2601ceb8027d41). 

### Lancement de l’impression

- Introduire la carte SD derrière l’écran LCD de l’imprimante.
- L’imprimante chargera les fichiers. Naviguez vers le nom de votre fichier et appuyez sur le bouton.
- L’imprimante prendra quelques minutes pour se chauffer. Une calibration sur 9 points sera faite, ensuite l’impression commencera.
- Il est important de surveiller les premières couches de l’impression afin de s’assurer que le modèle adhère au plateau.

!!! info "Ressources en ligne"

    [Première impression avec PrusaSlicer](https://help.prusa3d.com/fr/article/premiere-impression-avec-prusaslicer_1753)
    [Prusa Knowledge Base](https://help.prusa3d.com/fr/article/supports_1698)
    [Menu LCD i3 (pré firmware 3.9.0) | Prusa Knowledge Base](https://help.prusa3d.com/fr/article/menu-lcd-i3-pre-firmware-3-9-0_1876)

## Modifier la buse

![Outil spécial pour modifier la buse.](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2bb94673-2703-4455-9b95-4f86d96af0b9/IMG_20220423_104226.jpg)

1. Monter l’axe Z le plus haut possible. Attention à ne pas aller trop vite pour ne pas briser les moteurs!
2. Retirer le filament et la bobine du porte bobine.
3. Chauffer la buse à 280° C.
4. Dévisser la buse avec l’outil spécial. Attention aux fils, ne pas les pincer, ni les tordre, ni les arracher. Évitez que les parties en plastique ne touchent les parties chauffantes.
5. Retirer la buse de l’outil avec un pince (la buse est très chaude!) et poser la sur une surface qui ne craint pas la chaleur.
6. Visser la nouvelle buse pendant que le bloc est encore chaud (280° C). Assurez vous qu’il y ait environ 0,5 mm entre la buse et le bloc de chauffe, comme sur l’image suivante. Visser suffisamment la buse, mais sans exercer une force excessive.

![526a59ae1e9dcd1b_painted.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9e27cfb8-fa3c-4626-b56f-ec1dc90cf403/526a59ae1e9dcd1b_painted.png)

1. Attendre que ça refroidisse à environ 180° C.
2. Charger un filament.
3. Calibrer la première couche (*First layer calibration*). 

[Calibration de la première couche (i3) | Prusa Knowledge Base](https://help.prusa3d.com/fr/article/calibration-de-la-premiere-couche-i3_112364)

1. Dans PrusaSlicer, relancer le Configuration Wizard, et cocher la nouvelle buse utilisée afin que les paramètres soient par défaut.

<aside>
💡 [https://help.prusa3d.com/en/article/changing-or-replacing-the-nozzle-mk2-5s-mk3s-mk3s_2069](https://help.prusa3d.com/en/article/changing-or-replacing-the-nozzle-mk2-5s-mk3s-mk3s_2069)

</aside>