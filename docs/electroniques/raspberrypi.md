# Raspberry Pi

## Commandes utiles

Comme le Raspberry Pi s’opère aussi via les lignes de commandes, voici une liste non-exhaustive des commandes les plus utilisées :

- **sudo** : utilisé comme préfixe, il permet d’exécuter la commande avec des privilèges élevés.
- **apt-get update** : synchronise la liste des paquets du système. À faire avant d’effectuer une mise à jour.
- **apt-get upgrade** : met à jour les paquets présents dans le système.
- **apt-get dist-upgrade** : fait une mise à jour complète du système Raspbian.
- **apt-get install nomdupaquet** : installe un paquet en spécifiant son nom. Exemple : apt-get install vlc
- **apt-get remove nomdupaquet** : désinstalle un paquet.
- **clear** : efface le contenu texte du terminal.
- **date** : affiche la date actuelle.
- **find / -name exemple.txt** : cherche le fichier exemple.txt dans tout le système.
- **nano exemple.txt** : ouvre le fichier exemple.txt avec l’éditeur nano.
- **poweroff** : arrête le système immédiatement.
- **raspi-config** : ouvre le menu de configuration de Raspbian.
- **reboot** : redémarre le système.
- **shutdown -h now** : arrête le système.
- **shutdown -h 10:02** : arrête le système à une heure précise.
- **startx** : ouvre l’interface graphique de Raspbian.
- **flèche du haut** : revient vers la commande précédente.

### Commandes pour les fichiers et dossiers

- **cat exemple.txt** : affiche le contenu du fichier exemple.txt.
- **cd /test** : accède au dossier nommé test.
- **cd …** : revient en arrière.
- **cp exemple.txt /home/pi/test** : copie le fichier exemple.txt vers le dossier spécifié.
- **ls -l** : liste les fichiers présents dans le dossier avec la taille, la date de modification et les permissions.
- **mkdir test** : crée un nouveau dossier test.
- **mv exemple.txt /home/pi/test** : déplace le fichier exemple.txt vers le dossier test.
- **mv exemple.txt exemple1.txt** : renomme le fichier.
- **rm exemple.txt** : efface le fichier.
- **rmdir test** : efface le dossier (uniquement s’il est vide).
- **touch exemple.txt** : crée un nouveau fichier exemple.txt vide.

### Commandes réseaux et internet

- **Ifconfig** : vérifie le statut de la connectivité.
- **Iwconfig** : le nom du réseau wifi branché.
- **iwlist wlan0 scan** : affiche une liste des réseaux wifi disponibles.
- **nmap** : scan le réseau et liste les périphériques connectés, le nombre des ports, les protocoles, adresses MAC., etc.
- **ping [bib.umontreal.ca](http://bib.umontreal.ca/)** : teste la connectivité. Envoie un paquet à l’adresse et attend une réponse.
- **wget [bib.umontreal.ca/test.txt](http://bib.umontreal.ca/test.txt)** : télécharge le fichier test.txt depuis Internet et le sauvegarde dans le dossier courant.

### Commandes information système

- **ps aux** : liste des processus qui tournent.
- **kill pid** : termine le processus. Exemple : kill terminal.
- **cat /proc/meminfo** : affiche les détails sur la mémoire.
- **cat /proc/partitions** : affiche la taille et le nombre de partitions de la carte SD ou disque dur.
- **cat /proc/version** : affiche la version du Raspberry Pi utilisée.
- **df -h** : affiche des informations concernant les disques.
- **df /** : affiche combien d’espace libre il reste de disponible.
- **free** : affiche combien de mémoire vive il reste de disponible.
- **hostname -I** : l’adresse IP du Raspberry Pi.
- **lsusb** : affiche la liste des périphériques USB connectés au Raspberry Pi.
- **vcgencmd measure_temp** : affiche la température du CPU.

!!! info "Ressources en ligne"
    [Raspberry Pi online course](https://geek-university.com/raspberry-pi/raspberry-pi-online-course/)
    
    [How to open Terminal and use the command line - The MagPi magazine](https://magpi.raspberrypi.com/articles/terminal-help)

## Connexion au réseau UdeM avec cryptage sur Raspbian OS

### Étape 1 : Installer et activer le network-manager

Ouvrez la fenêtre de terminal et exécutez les commandes ci-dessous pour installer le gestionnaire de réseau Linux standard.

```bash
sudo apt install network-manager network-manager-gnome
sudo systemctl disable --now dhcpcd 
sudo systemctl enable --now network-manager
sudo reboot
```

La première ligne permet d'installer le gestionnaire de réseau.
La deuxième ligne permet de désactiver **DHCP**, car il ne fonctionnera pas avec le gestionnaire de réseau.
La troisième ligne permet d'activer le service de gestionnaire de réseau. 
La dernière ligne permet de redémarrer l'appareil.

Si **sudo systemctl enable NetworkManager** ne fonctionne pas, iI existe une autre façon d'activer **NetworkManager** sur Raspberry Pi en utilisant la commande **raspi-config**. Voici les étapes à suivre :

1. Ouvrez le gestionnaire de configuration en utilisant la commande :
`sudo raspi-config`
2. Allez à **Interfacing options.**
3. Sélectionnez **P2 Network.**
4. Choisir **N1 to enable the SPI interface.**
5. Redémarrer le système en utilisant la commande :
`sudo reboot`

**NetworkManager** devrait être activé et vous pourrez gérer vos connexions réseau en utilisant cet outil.

Il est important de noter que cette méthode n'est valable que pour les versions récentes de Raspbian et qu'il est possible que cette option n'apparaisse pas dans l'interface si vous utilisez une version antérieure.

### Étape 2 : Connexion à UdeM avec cryptage

1. Téléchargez le [certificat d'authentification](https://entrust.com/root-certificates/entrust_g2_ca.cer?_ga=2.176382957.952316860.1542655212-1390703555.1542655212).
2. Aller dans les paramètres **WI-FI** (habituellement en haut à droite de l'écran)
3. Sélectionner le réseau **UdeM avec cryptage**
4. Appliquez les paramètres suivants :
- Dans le champ **Sécurité**, choisissez **WPA et WPA2 d'entreprise**.
- Dans le champ **Authentification**, sélectionnez **EAP sécurisé (PEAP**).
- Dans le champ **Certificat CA**, indiquez l'emplacement où vous avez sauvegardé la clé de chiffrement.
- Dans le champ **Nom d'utilisateur**, inscrivez votre **code d'accès TI** .
- Dans le champ **Mot de passe**, entrez votre **mot de passe/UNIP** de votre compte.

### Pour aller plus loin

Il existe plusieurs autres façons de le faire, si jamais vous n’arrivez toujours pas a vous connecter à un réseau d’entreprise, en voici quelques-unes :

#### Mode Hotspot

Activer le mode hotspot sur un portable, voici les étapes à suivre (les étapes peuvent varier légèrement en fonction du système d'exploitation et du modèle de téléphone) :

- Accédez aux paramètres de votre téléphone.
- Recherchez l'option **Partage de connexion, Hotspot personnel, point d'accès mobile** ou **tethering**.
- Activez l'option **Hotspot personnel** ou **partage de connexion**.
- Configurez les paramètres de sécurité pour votre hotspot (par exemple, nom du réseau et mot de passe).
- Connectez les appareils à votre hotspot en utilisant les informations de connexion configurées.


!!! info "Important"
    L'utilisation de la fonctionnalité de partage de connexion peut consommer beaucoup de données et peut entraîner des frais supplémentaires de votre fournisseur de services. Assurez-vous de vérifier les limites de données de votre forfait avant d'utiliser cette fonctionnalité.


#### Connexion à un réseau filaire

Si votre Raspberry Pi est équipé d'une carte Ethernet, vous pouvez connecter directement le Raspberry Pi à un réseau câblé d'entreprise en utilisant un câble Ethernet.

#### Connexion WIFI

Vous pouvez également connecter votre Raspberry Pi à un réseau WiFi d'entreprise en utilisant une carte WIFI USB ou intégrée. Il vous faudra configurer les paramètres de connexion WiFi en utilisant l'outil de gestion de connexion **Network Manager** ou **wpa_supplicant**.

#### Connexion VPN

Si votre réseau d'entreprise utilise un VPN, vous pouvez configurer un client VPN sur votre Raspberry Pi pour vous connecter à ce réseau. Il existe plusieurs clients VPN open-source que vous pouvez installer sur votre Raspberry Pi, tels que **OpenVPN** ou **StrongSwan**.

!!! info "Ressources en ligne"
    [Configurer le réseau sans-fil sur un poste Linux](https://wiki.umontreal.ca/display/SIE/FAQ+Linux)