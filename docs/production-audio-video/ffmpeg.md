

# FFmpeg

**FFMPEG** est un puissant convertisseur audio/vidéo open-source compatible Linux, Mac et Windows. Il fonctionne en ligne de commande. Ce mode de fonctionnement peut vous paraître difficile à première vue, mais une fois initié, vous allez aimer cet outil. Vous utilisez probablement déjà un logiciel qui utilise ffmpeg : Kodi, VLC, Blender, Adobe Premiere Pro, etc.

## Installation

### sur Windows

[Télécharger la dernière version pour Windows](https://www.gyan.dev/ffmpeg/builds/), décompresser et renommer le dossier en ffmpeg et le mettre sur c:\ (à côté de program files et windows). Ensuite, clic droit sur l’icône **Ordinateur > Propriétés Systèmes > Variable d’environnements**. Chercher **PATH** et ajouter à la fin (sans effacer le contenu) **;C:\ffmpeg**. Pour tester, il suffit d’ouvrir MS-DOS et taper **ffmpeg**.

Il existe deux tutoriels très pratique sur comment installer ffmpeg sur Windows. Nous vous recommandons le premier lien.

[http://adaptivesamples.com/how-to-install-ffmpeg-on-windows/](https://web.archive.org/web/20211021224811/http://adaptivesamples.com/how-to-install-ffmpeg-on-windows/)

[http://fr.wikihow.com/installer-FFmpeg-sur-Windows](https://web.archive.org/web/20211021224811/http://fr.wikihow.com/installer-FFmpeg-sur-Windows)

Vous êtes sur Windows 10? [Il est possible de lancer Bash directement depuis Win10.](https://web.archive.org/web/20211021224811/http://www.numerama.com/tech/158150-le-shell-bash-sous-windows-10-ce-quil-faut-savoir.html)

### sur MacOS

Un moyen pratique d’installer ffmpeg est de faire appel au gestionnaire de paquets sous MacOS [Homebrew](http://brew.sh/index_fr.html). Pour installer Homebrew, ouvrir le terminal :

++cmd+space++ et tapez **terminal** ou allez à **Application/Utilitaires/Terminal**.

Une fois le terminal ouvert, tapez cette commande :

```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

Un mot de passe administrateur vous sera peut-être demandé.
Une fois Homebrew installé, il suffit de taper cette commande pour installer ffmpeg :

```bash
brew install ffmpeg
```

vous pouvez aussi exécuter cette commande pour avoir ffmpeg avec les dépendances recommandées :

```bash
brew install ffmpeg --with-fdk-aac --with-ffplay --with-freetype --with-libass --with-libquvi --with-libvorbis --with-libvpx --with-opus –with-x265
```

Pour s’assurer d’avoir la dernière version de Homebrew et de ffmpeg, exécutez cette commande :

```bash
brew update && brew upgrade ffmpeg
```

Tapez **ffmpeg** via le terminal. Si le terminal renvoie le numéro de la version et les dépendances installées, vous êtes prêt à l'utiliser. 

## Premier pas

Testons les possibilités de ce logiciel.

Munissez-vous d’une vidéo pour faire les tests. Utilisez une de vos vidéos ou téléchargez-en à partir de ce lien : [http://www.h264info.com/clips.html](https://web.archive.org/web/20211021224811/http://www.h264info.com/clips.html)

Pour ce tutoriel, on va utiliser le trailer de Gravity en 2K (2048×858), un ratio cinémascope de ~2.39:1, encodé en H.264 avec un son en AAC et un conteneur Mpeg4.

Changer le nom en **vid0.mp4** et placer dans un répertoire appelé **conversion** sur le bureau.
Depuis le terminal, on va pouvoir accéder au fichier. 
Pour cela, deux commandes sont à retenir : **ls** et **cd**.

**ls** permet de lister tous les fichiers et dossiers qui se trouvent dans le répertoire actuel et **CD** permet d’accéder à des répertoires.

Tapez **ls**

Vu que le dossier **conversion** se trouve dans le répertoire **desktop**, tapez :

```bash
cd desktop/conversion
```

Vous allez voir apparaître le nom du répertoire avant le nom d’utilisateur.
Ensuite, tapez **ls** pour s’assurer que notre fichier se trouve bien dans ce répertoire.

À chaque opération, on va retrouver le fichier de sortie dans notre dossier **conversion**. Pendant la conversion, une ligne apparaît avec plusieurs informations qui nous indiquent à quel niveau est rendue la conversion, la vitesse par rapport à une lecture en temps réel, le débit binaire *bitrate*, etc.

Vous pouvez, à tout moment, arrêter la conversion en appuyant sur la touche **Q** ou ++ctrl+c++

## Pour avoir de l’aide

```bash
ffmpeg -h
```

## Extraire le son seul

```bash
ffmpeg -i vid0.mp4 -vn -f ac3 audio0.mp3
```

- le **-i** représente l’input, il est suivi du nom du fichier présent dans le dossier.
- le **-vn** va désactiver la vidéo
- le **-f** va forcer le format d’entrée ou de sortie
- **ac3** est le type de codec qu’on va utiliser
- et enfin **audio0.mp3** est le nom de notre fichier de sortie.

Une autre façon d’extraire le son mais avec plus de configuration :

```bash
ffmpeg -i vid0.mp4 -ac 2 -ar 44100 -vn -b:a 256k audio1.mp3
```

- **-ac 2** détermine le nombre de canaux à 2
- **-ar** détermine le taux d’échantillonnage, défini à 44100. Si on n’utilise pas cette fonction, il sera par défaut le même nombre que l’entrée.
- **-b:a** détermine le débit (*bitrate*), définit à 256k.

## Désactiver le son

```bash
ffmpeg -i vid0.mp4 -an vid1.mp4
```

- **-an** va désactiver le son.

## Redimensionner

```bash
ffmpeg -i vid0.mp4 -vf scale=640:268 vid1.mp4
```
- **-vf scale=** agit comme un filtre pour redimensionner la vidéo dans le format de notre choix.

Attention ! Respectez les proportions. Ma vidéo a un ratio de 2.39:1 (2048/858). Pour 640 en largeur, il faut diviser par 2.39 pour avoir la hauteur.

À titre d’information, le ratio du 16/9 est de 1.77:1.

On peut aussi utiliser la fonction **scale=x:-1** qui va garder la proportion de la vidéo.

```bash
ffmpeg -i vid0.mp4 -vf scale=640:-1 vid1.mp4
```

## Changer la durée

```bash
ffmpeg -i vid0.mp4 -t 80 vid1.mp4
```
- **t 80** va déterminer la durée de la vidéo à 80 secondes.

```bash
Ffmpeg i vid0.mp4 -ss 90 vid1.mp4
```
- **ss** va commencer la lecture après 90 secondes.

Il est possible de mélanger nos fonctions en une seule ligne. Exemple :

```bash
ffmpeg -i vid0.mp4 -vf scale=640:268 -ss 90 -t 80 -an vid1.mp4
```
Si on utilise à chaque fois le même nom en sortie (**vid1.mp4** dans notre cas) ffmpeg va nous demander si on veut écraser le fichier. Si oui, tapez **Y**.

## Pour avoir des informations sur notre vidéo

```bash
ffmpeg -i vid0.mp4
```
Ces informations seront précieuses pour la suite, comme le codec, le format, le *bitrate*, *framerate*, etc.

## Couper une section d’une vidéo

```bash
ffmpeg -i vid0.mp4 -ss 00:00:10 -t 00:00:05 vid1.mp4
```
Prends seulement 5 secondes à partir de la 10ème seconde.

## Rotation d’une vidéo

```bash
ffmpeg -i vid0.mp4 -vf rotate=45 vid1.mp4
```
Une rotation de 45°.

## Conteneur

Pour connaître la liste des conteneurs (formats) disponibles sous ffmpeg, tapez :

```bash
ffmpeg -formats
```

Cette fonction va tout simplement changer de format du .mp4 en .mov :

```bash
ffmpeg -i vid0.mp4 -codec copy vid1.mov
```

On peut même forcer une extension :

```bash
ffmpeg -i vid0.mp4 -f mp4 -codec copy vid0.udem
```

...et ça marche. On peut même le lire via VLC puisque le contenu, en H.264, est resté intact.

## Codecs

Pour connaître la liste des codecs :

```bash
ffmpeg -codecs
```

On va ré-encoder notre vidéo au format ProRes :

```bash
ffmpeg -i vid0.mp4 -codec:v prores vid1.mov
```
On a, à la fois, changé le contenu et le contenant (le codec et le format).

Pour convertir en h264 :

```bash
ffmpeg -i vid0.mp4 -vcodec h264 vid1.mov
```

Sachez que vous pouvez utiliser **-codec:v**, **-vcodec** ou encore mieux, **-c:v**.

## Bitrate

```bash
ffmpeg -i vid0.mp4 -b:v 5000k vid1.mp4
```

Le *bitrate* (taux d’échantillonnage) est de 5Mo/s.

Plus le *bitrate* est haut, meilleure est la qualité. Par exemple, Youtube recommande 8000k pour une vidéo de 1080p avec une fréquence d’image standard (24, 25 et 30).

[Paramètres d’encodage Youtube.](https://support.google.com/youtube/answer/1722171?hl=fr)
[Paramètres d’encodage Vimeo.](https://vimeo.com/help/compression)

## Deux vidéos bout à bout

```bash
ffmpeg -i vid0.mp4 -i vid1.mp4 -filter_complex "[0:v] [1:v] concat=n=2:v=1:a=0 [v]" -map "[v]" -vcodec h264 vidfinal.mp4
```

## *Overlay* (superposition)

Dans le même répertoire, inclure un png (un format qui supporte la transparence) pour faire une superposition sur la vidéo. 


```bash
ffmpeg -i vid0.mp4 -i udem-logo.png -filter_complex "[0:v][1:v]overlay[out]" -map "[out]" vid1.mp4
```

Cette commande est bien pratique si jamais on veut faire un *watermark* sur une série de vidéos.

On peut aussi superposer une vidéo :

```bash
ffmpeg -i vid0.mp4 -i vid1.mp4 -filter_complex "[0:v][1:v]overlay=x=200:y=100[out]" -map "[out]" -t 20 vidfinal.mp4
```

Vous remarquez ici qu’on a spécifié des coordonnées en x et y de la deuxième vidéo qu’on veut superposer, et une fonction **-t 20** qui va juste faire une conversion de 20 secondes de la vidéo. La fonction **-t** peut aussi être placée avant les vidéos en input. (Exemple : `ffmpeg -t 10 -i vid0.mp4`)

## *Crop* (rogner)

```bash
ffmpeg -i vid0.mp4 -filter:v crop=320:180:160:90 vid1.mp4
```

Autrement dit, la largeur (*width*) est de 320, la hauteur (*height*) est de 180, avec des coordonnées x de 160 et y de 90.

Cela peut s'écrire ainsi aussi :

```bash
ffmpeg -i vid0.mp4 -filter:v crop=w=320:h=180:x=160:y=90 vid1.mp4
```

## Extraire une série d’images

Dans cet exemple, on va extraire les deux premières secondes en une série d’image avec des noms qui se suivent :

```bash
ffmpeg -i vid0.mp4 -r 24 -t 2 -f image2 img-%04d.png
```

La valeur **-r 24** correspond au nombre d’images par seconde de la vidéo vid0.mp4 (24fps).

## Combiner des images pour en faire une vidéo

Il faut que les noms des images se suivent. Dans cet exemple, ça va être 001.jpg, 002 jpg, etc.

Si jamais il y a un texte avant les numéros, par exemple img-, n’hésitez pas à l’ajouter avant le %03d.jpg, ce qui va donner img-%03d.jpg. Le rendu va être par défaut à 25fps et 200kbps. %03d représente le nombre de chiffres après le texte (%03d = img-001.jpg / %04d = img-0001.jpg et ainsi de suite.)

```bash
ffmpeg -i %03d.jpg test.mp4
```

Cette commande est pratique pour créer des animations *stopmotion* ou *timelapse*.

Un autre moyen mais avec plus de personnalisation :

```bash
ffmpeg -framerate 60 -i image-%04d.jpg -start_number 1 -r 60 -c:v libx264 -crf 25 -pix_fmt yuv420p pattern60.mp4

```

- **framerate** : à mettre avant l’input pour spécifier combien d’images à lire en input par seconde.
- **start_number** : par quelle image il faut commencer
- **vframes** : combien d’image à utiliser
- **– r** : combien d’images par seconde
- **c:v libx264 -crf 25 -pix_fmt yuv420p** : ceci va permettre d’encoder en H264, sans perte de qualité et en 4.2.0.
- **i image-%04.jpg** : le 04 représente le nombre de chiffres qui suit le texte image- (image-0001, image-0002, etc.)

Attention ! Une valeur **img-*.png** doit s’écrire ainsi : **-pattern_type glob -i « image-*.png »**

**img-*.png** est valable aussi pour les chiffres. 15 vient avant 110 mais parfois, le système met 110 avant 15. Pour être sûr, tapez dans le terminal **echo img-*.png** pour connaître comment votre système liste les numéros.

## Boucle (*loop*)

Faire une boucle de 30 secondes d’une vidéo :

```bash
ffmpeg -i loop 1 -i input.mp4 -t 30 out.mp4
```

## Luminosité 
Par un facteur de 4 :
```bash
ffmpeg -i vid0.mp4 -vf lutyuv=y=val*4 vidlum.mp4
```

Seulement le rouge par 2 :
```bash
ffmpeg -i vid0.mp4 -vf lutyuv=r=val*2 vidr.mp4
```

## Faire un rendu en noir et blanc

```bash
ffmpeg -i vid0.mp4 -vf hue=s=0 -c:a copy vidnb.mp4
```

## Teinte

```bash
ffmpeg -i vid0.mp4 -vf hue=h=90:s=1 -c:a copy vidteinte.mp4
```

La teinte est à 90° et la saturation à 1.

On peut aussi s’amuser à faire tourner la teinte et balancer la saturation entre 0 et 2 chaque 1 seconde.

```bash
ffmpeg -i vid0.mp4 -vf hue="H=2*PI*t: s=sin(2*PI*t)+1" -c:a copy vidtcolor.mp4
```

## Appliquez un *Fade-In* de 30 images

```bash
ffmpeg -i vid0.mp4 -vf fade=in:0:30 -c:a copy vidfadin.mp4
```

On peut aussi appliquer un noir de 5 secondes, ensuite un fade-in de 0.5 seconde :

```bash
ffmpeg -i vid0.mp4 -vf fade=t=in:st=5:d=0.5 -c:a copy vidfadin.mp4
```

## Réduction du bruit

```bash
ffmpeg -i vid0.mp4 -vf "split [main][tmp]; [tmp] dctdnoiz=4.5 [tmp2]; [main][tmp2] overlay" vidfinal.mp4
```

## *Splitscreen* (une vidéo de chaque côté)

```bash
ffmpeg -i vid0.mp4 -i vid1.mp4 -filter_complex "[0:v:0]pad=iw*2:ih[bg];[bg][1:v:0]overlay=w" out.mp4
```

## Conclusion

C’est bien plus pratique d’utiliser ffmpeg que de passer par un logiciel de montage vidéo pour exécuter des fonctions simples. Cela représente un gain de temps non négligeable dans la production vidéo et audio, surtout s’il s’agit de faire la même action (encoder, superposer un *watermark*, *fade-in*, *splitscreen* pour un aperçu multicam, etc.). L’autre avantage est que ffmpeg est gratuit, libre et open source et qu’il dispose d’une communauté importante avec une documentation complète.

!!! Info "Ressources en ligne"
    - Le site de ffmpeg avec une documentation complète [https://ffmpeg.org/](https://web.archive.org/web/20211021224811/https://ffmpeg.org/)
    - Le site de Homebrew [http://brew.sh/](https://web.archive.org/web/20211021224811/http://brew.sh/)
    - Tutoriels installation sur Windows :
        - (EN) [http://adaptivesamples.com/how-to-install-ffmpeg-on-windows/](https://web.archive.org/web/20211021224811/http://adaptivesamples.com/how-to-install-ffmpeg-on-windows/)
        - (FR) [http://fr.wikihow.com/installer-FFmpeg-sur-Windows](https://web.archive.org/web/20211021224811/http://fr.wikihow.com/installer-FFmpeg-sur-Windows)
    - Vidéos pour les essais [http://www.h264info.com/clips.html](https://web.archive.org/web/20211021224811/http://www.h264info.com/clips.html)
    - Instructions de compression des vidéos Vimeo [https://vimeo.com/help/compression](https://web.archive.org/web/20211021224811/https://vimeo.com/help/compression)
    - et Youtube [https://support.google.com/youtube/answer/1722171?hl=fr](https://web.archive.org/web/20211021224811/https://support.google.com/youtube/answer/1722171?hl=fr)
    - Un tutoriel assez complet pour utiliser la console du terminal [https://openclassrooms.com/courses/domptez-votre-mac-avec-mac-os-x-mavericks/le-terminal-dans-os-x](https://web.archive.org/web/20211021224811/https://openclassrooms.com/courses/domptez-votre-mac-avec-mac-os-x-mavericks/le-terminal-dans-os-x)