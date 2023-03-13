---

date: 2022-01-31
authors:
  - AnneJulie
categories:
  - Arduino
links : 
  - doc/se/arduino/

---

# Plante intelligente

Comment faire ceci. 

<!-- more -->

Il existe dans le marché une multitude de capteurs pour mesurer l’humidité du sol. Certains, en contact de l’eau, se détériorent très vite, devenant alors inutilisables et [pouvant présenter un risque pour la plante](http://kstobbe.dk/2019/01/13/effectively-killing-a-plant/). [La vidéo suivante](https://www.youtube.com/watch?v=udmJyncDvw0) présente un comparatif de différents capteurs. Notre choix se porte sur le capteur [Capacitive Soil Moisture Sensor V 2.0](https://fr.aliexpress.com/item/32832538686.html?spm=a2g0s.9042311.0.0.41a86c37TOYxzS), coutant environ 2$. Afin de mieux le protéger contre la corrosion dû au contact prolongé avec l’eau, on applique une fine couche de vernis uniquement sur les bords. Une fois séché, le vernis va prévenir la détérioration du capteur.

## Les étapes

### Étape 1 : Connecter le capteur d’humidité

Le schéma a été fait avec [Fritzing](https://fritzing.org/), un logiciel libre pour la conception des circuits électroniques.

Dans la version actuelle du logiciel, le capteur qui a été utilisé n’est pas encore répertorié, d’où l’image d’un autre capteur d’humidité du sol, celui de Sparkfun.

Le capteur possède trois broches :

- **VCC** se connecte à la broche **5V**.
- **GND** se connecte dans le **GND** de l’Arduino.
- **AUOT** se connecte dans la broche **A0**, ce qui va nous permettre de lire les valeurs.

### **Étape 2 : Tester le capteur**

Une fois que le capteur est connecté, on branche l’Arduino à l’ordinateur et on lance le logiciel Arduino IDE. Si vous ne l’avez pas encore installé, consultez [ce guide de démarrage](https://www.notion.so/fb66bae70ca447598a85efcf454353e8). C’est aussi une bonne idée d’ouvrir [la page référence](https://www.arduino.cc/reference/en/).

On veut lire les valeurs envoyées par le capteur. Pour cela, on aura besoin d’un verre rempli à moitié d’eau afin d’y plonger le bout du capteur.

Notre capteur est **analogique**, c’est-à-dire qu’il va nous donner des valeurs en voltage de **0** à **1023**.

```arduino
int valeurCapteur; // on crée une variable pour stocker les valeurs

void setup() {
Serial.begin(9600); // initialise la communication en série à 9600bits/s
}

void loop() {
valeurCapteur = analogRead(A0);
Serial.println(valeurCapteur);
delay(500);
}
```

Après le téléversement du code, aller dans **Outils > Moniteur série**. Vous allez voir des valeurs. Si vous mettez le capteur dans le verre d’eau, celui-ci réagit et les valeurs seront à la baisse.

### **Étape 3 : Les valeurs du capteur**

On va faire réagir la **DEL 13** en donnant une condition et une valeur à Arduino: La **DEL 13** doit s’allumer si la valeur descend au-dessous de **500**.

La **DEL 13** est déjà intégrée à la carte Arduino. Elle est encerclée en vert dans le schéma ci-contre.

![https://i.imgur.com/pA1PLAF.png](https://i.imgur.com/pA1PLAF.png)

```arduino
int valeurCapteur;
int limite = 500; // valeur sous laquelle la LED s’allumera

void setup() {
Serial.begin(9600);
pinMode(13, OUTPUT); // la connexion 13 doit pouvoir envoyer du courant
}

void loop() {
valeurCapteur = analogRead(A0);
Serial.println(valeurCapteur);
delay(500);

if (valeurCapteur>limite) {
digitalWrite(13,LOW); // ne pas envoyer du courant dans la connexion 13, la plante a soif
}
else {
digitalWrite(13,HIGH); // envoyer du courant dans la connexion 13, la plante n'as plus soif
}
}
```

Si on retire ou on remet le capteur dans le verre d’eau, on va voir la DEL réagir ! N’hésitez pas à surveiller les valeurs via le moniteur série.

En présence d’eau, le capteur affiche 247 et en son absence, 592. Il est fort probable que vous ayez des valeurs différentes. On utilise la fonction `map()` pour retranscrire ces valeurs en pourcentage.

```arduino
valeurSenseur = map(valeurSenseur,592,247,0,100);
```

> Pour en savoir plus sur la fonction `map()`, consultez [la page référence Arduino](https://www.arduino.cc/reference/fr/).
> 

### **Étape 4 : Branchement des DELs**

Connectons les DELs pour avoir une indication en rouge lorsque la plante a soif et en vert lorsqu’elle est suffisamment hydratée. Voici le nouveau schéma :

![https://i.imgur.com/pM1ewmv.png](https://i.imgur.com/pM1ewmv.png)

### **Étape 5 : Téléverser le code**

```arduino
int pinSenseur = A0;
int valeurSenseur;
int limite = 50;

void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  pinMode(12, OUTPUT);
}

void loop() {
  valeurSenseur = analogRead(pinSenseur);
  valeurSenseur = map(valeurSenseur,592,247,0,100);
  delay(500);
  Serial.println(valeurSenseur);

  if (valeurSenseur<limite) {
    digitalWrite(13,LOW);
    digitalWrite(12,HIGH);
  }
  else {
    digitalWrite(13,HIGH);
    digitalWrite(12,LOW);
  }
}
```

## **Photos du projet**

![SC_AFN (4).jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ff9b43f9-b519-49c7-8625-6e982a8f75b1/SC_AFN_(4).jpg)

![SC_AFN (5).jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3cb03f77-edfb-4ac1-8dc2-1a11948b9c82/SC_AFN_(5).jpg)

## **Pour aller plus loin**

Le projet peut être amélioré de plusieurs façons :

- Une DEL : utiliser une seule DEL vert/rouge au lieu de deux DEL.
- Écran LCD : connecter un écran pour afficher l’état, afficher les données relatives à l’humidité en remappant les valeurs en pourcentage ou tout simplement afficher du texte comme “j’ai soif!”.
- Internet des objets : utiliser un autre microcontrôleur, comme l’ESP8266, afin d’envoyer les données à distance et de connaître l’état du sol en temps réel.
- Pompe à eau : contrôler l’arrosage automatiquement, en fonction du niveau d’humidité.
