# OBS

## Introduction

OBS est un logiciel gratuit et libre pour enregistrer des vidéos et même diffuser sur les plateformes de diffusion en continu comme Twitch ou YouTube. Cet outil permet de mélanger différentes sources audio et vidéo et de les disposer comme bon nous semble dans un canevas. 

### Cas d’usages

- Capture de caméra, écran et audio.
- Événement en ligne.
- Création de vidéos pédagogiques.

### Quelques avantages

- Outil puissant et fiable pour la capture.
- Création de contenu avec plusieurs scènes différentes, sans perte de temps en post-production.

## Télécharger et installer le logiciel

OBS est gratuit, libre et compatible Windows, MacOS et Linux. [Télécharger la dernière version depuis le site officiel](https://obsproject.com/fr). 

## Première configuration

- Au lancement du logiciel la première fois, la fenêtre **Assistant de configuration automatique** apparait. Sélectionner **Optimiser pour l’enregistrement, je ne diffuse pas** et cliquer sur **Suivant.**
    
    ![Capture d’écran 2022-11-21 100231.webp](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e701541e-c2d3-432f-8d48-cc63c0245cf2/Capture_dcran_2022-11-21_100231.webp)
    
    <aside>
    💡 Si la fenêtre ne s’affiche pas au démarrage, vous pouvez lancer l’assistant en cliquant dans le menu en haut sur **Outils > Assistant de configuration automatique.**
    
    </aside>
    

- Dans **Paramètres vidéo**, choisir **Garder tel quel** et sélectionner **30** dans le **débit d’images (FPS)**. Cliquer sur **Suivant** puis **Appliquer les paramètres**.
    
    ![Capture d’écran 2022-11-21 100302.webp](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/bc831b51-5776-447a-aa33-3b8f04c77c4d/Capture_dcran_2022-11-21_100302.webp)
    

- Au lancement de l’interface, cliquer sur **Paramètres** en bas à droite.
- Dans l’onglet **Avancé**, cocher la case **Convertir automatiquement en MP4** dans la section Enregistrement puis sur **OK** en bas de la fenêtre.
    
    ![Capture d’écran 2022-11-21 100404.webp](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/bbb07338-86e2-4a91-9426-64c7f28ccc6c/Capture_dcran_2022-11-21_100404.webp)
    

## Ajouter des sources

<aside>
💡 Pour des raisons pratiques, l’aperçu de la webcam a été remplacé par un personnage.

</aside>

- Dans **Sources**, appuyer sur le bouton **+** pour ajouter une source au canevas.
    
    ![Capture d’écran 2022-11-21 100547.webp](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/cf6aa3e8-21ea-4895-ac10-2e4599de5eda/Capture_dcran_2022-11-21_100547.webp)
    

- Sélectionner **Périphériques de capture vidéo**
    
    ![Capture d’écran 2022-11-21 100608.webp](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b0f0b2d2-4a8d-49a6-b5fe-6b1a765705d2/Capture_dcran_2022-11-21_100608.webp)
    
- Sélectionner **Créer/Sélectionner une source** et choisir un nom.
    
    ![Capture d’écran 2022-11-21 100630.webp](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a29a7d4c-f37d-4c52-9657-2fa5ca7c80a1/Capture_dcran_2022-11-21_100630.webp)
    
- Voici les paramètres à changer dans les propriétés :
    - **Périphériques** : Sélectionner votre caméra.
    - **Type de résolution/FPS** : Personnalisé.
    - **Résolution** : Choisir 1920x1080
    - **FPS** : identique à la sortie
        
        ![Capture d’écran 2022-11-21 100714.webp](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/aa6eb855-1e6c-4c7f-9996-e46a471b5294/Capture_dcran_2022-11-21_100714.webp)
        
- Une fois validé, voici à quoi ressemblerait l’interface :
    
    ![Capture d’écran 2022-11-21 100733.webp](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6d94e48f-638c-4045-8ed3-9dd498b3c26e/Capture_dcran_2022-11-21_100733.webp)
    

## Ajouter une source sonore

Par défaut, OBS capture le micro du système, c’est à dire que si votre PC portable est équipé d’un micro interne, c’est le micro qui va être utilisé. 

Afin de changer cela, vous devez rajouter dans **Sources > Capture Audio (Entrée)** et sélectionner votre périphérique de capture sonore. 

![Capture d’écran 2022-11-21 105305.webp](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2c7d3a42-da0d-4d5a-a691-40b6cfe7e3ef/Capture_dcran_2022-11-21_105305.webp)

Ne pas oublier de baisser le volume dans le **Mélangeur audio** de la source **Mic/Aux** et de **Caméra** à **0** afin de ne capturer que l’entrée que vous avez choisie. 

![Capture d’écran 2022-11-21 113653.webp](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d4ef71ab-4af5-4f65-a215-5003f32b64fe/Capture_dcran_2022-11-21_113653.webp)

## Capturer l’écran

Toujours dans Sources, vous avez le choix de capturer tout l’écran (**Capture d’écran**) ou seulement la fenêtre d’une application (**Capture de fenêtre**).

## Modifier l’ordre et la disposition des sources

Dans l’onglet **Sources**, vous pouvez glisser/déposer les entrées afin de changer quelle source sera en arrière-plan ou en avant-plan, dans le même esprit que le principe des calques dans Photoshop. 

![Animation.gif](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a9ca1d06-d387-4a2b-8ba8-ea0fb58d845b/Animation.gif)

Vous pouvez aussi changer la taille des sources dans le canevas :

![Animation1.gif](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f94bd6e8-c73b-40d6-b8f7-e410e96ac71d/Animation1.gif)

## **Enregistrement et exportation**

Pour commencer à enregistrer, cliquer sur le bouton **Démarrer l’enregistrement** dans l’onglet Commandes en bas à droite. Vous avez par la suite la possibilité de faire des pauses ou d’arrêter l’enregistrement. Par défaut, les vidéos vont être enregistrées dans le dossier **/*Username*/Vidéos.** Vous pouvez changer le chemin de destination dans **Paramètres > Sortie > Enregistrement > Chemin d’accès de l’enregistrement**. 

Vous remarquerez qu’il y a deux fichiers vidéos pour un seul enregistrement : l’un avec l’extension **.mkv**, l’autre en **.mp4**. La raison est que si jamais vous voulez faire des pauses en cours d’enregistrement, il risque d’y avoir moins d’erreur avec le conteneur **.mkv**. Par la suite, **OBS** convertit cet enregistrement en **.mp4** pour le montage. Vous pouvez donc effacer les **.mkv** pour libérer de l’espace et garder le **.mp4**.