// Appel aléatoirement une image de fond pour la page d'accueil
// Tout en gardant le gradient avec les couleurs de la charte graphique

function getRandomInt(max) {
  return Math.floor(Math.random() * Math.floor(max));
}

var images = [
    'assets/images/hero1.webp',
    'assets/images/hero2.webp',
    'assets/images/hero3.webp',
    'assets/images/hero4.webp',
    'assets/images/hero5.webp',
    'assets/images/hero6.webp',
    'assets/images/hero7.webp'
];

var randomIndex = getRandomInt(images.length);
var randomImage = images[randomIndex];
document.body.style.backgroundImage = "linear-gradient(rgba(0, 0, 0, 0.850), rgba(0, 87, 172, 0.60))," + 'url(' + randomImage + ')';