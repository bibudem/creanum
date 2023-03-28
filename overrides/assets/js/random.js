// Appel aléatoirement une image de fond pour la page d'accueil
// Tout en gardant le gradient avec les couleurs de la charte graphique

function herobg(){
    var random= Math.floor(Math.random() * 7) + 0;
    var bigSize = ["url('assets/images/hero1.webp')",
                   "url('assets/images/hero2.webp')",
                   "url('assets/images/hero3.webp')",
                   "url('assets/images/hero4.webp')",
                   "url('assets/images/hero5.webp')",
                   "url('assets/images/hero6.webp')",
                   "url('assets/images/hero7.webp')"];
    document.getElementById("hero").style.background="linear-gradient(rgba(0, 0, 0, 0.850), rgba(0, 87, 172, 0.60))," + bigSize[random] + "no-repeat center / cover";
  }
