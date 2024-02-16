//////////////////////  ANIMATION PAGE ////////////////////////

const sideMenu = document.querySelector("aside");
const menuBtn = document.querySelector("#menu-btn");
const closeBtn = document.querySelector("#close-btn");
const pumpBtn = document.querySelector("#pump-btn"); 
const dashboardBtn = document.querySelector("#dashboard-btn"); 


menuBtn.addEventListener('click', () =>{
    sideMenu.style.display = 'block';
})

closeBtn.addEventListener('click', () =>{
    sideMenu.style.display = 'none';
})

pumpBtn.addEventListener('click', () => {
    window.location.href = 'pump1.html'; // Redirige vers pump1.html
});

dashboardBtn.addEventListener('click', () => {
    window.location.href = 'index.html'; 
});


//////////////////  DATA LOAD  ////////////////////////////

document.addEventListener('DOMContentLoaded', function() {
    fetchDataAndUpdateUI();
    setInterval(fetchDataAndUpdateUI, 5000); // Rafraîchit les données toutes les 5 secondes
});

function fetchDataAndUpdateUI() {
    fetch('../data.json') 
        .then(response => response.json())
        .then(data => {
            const fromSystem = data.fromSystem || {}; // Fournit un objet vide par défaut
            const temperature = fromSystem.temperature || 'N/A'; // Utilise 'N/A' comme valeur par défaut
            const tds = fromSystem.tds || 'N/A';

            // Mise à jour de l'interface utilisateur avec les nouvelles valeurs
            document.querySelector('.temperature .middle .left h1').innerText = `${temperature}°C`;
            document.querySelector('.tds .middle .left h1').innerText = `${tds}ppm`;
        })
        .catch(error => console.error('Error fetching data:', error)); // Gestion des erreurs
}

///////////////// USER DATA /////////////////////////////
const pump1OnSlider = document.getElementById('pump1-on-slider');
const pump1OnValueDisplay = document.getElementById('pump1-on-value');


document.getElementById('pump1-on-slider').addEventListener('input', function() {
    const pump1OnValue = this.value;
    document.getElementById('pump1-on-value').innerText = `${pump1OnValue} min`; // Affiche la valeur actuelle du slider

    // Envoie la nouvelle valeur au serveur
    fetch('/update-pump-interval', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ fromUser: { pump1OnValue: pump1OnValue }}),
    })
    .then(response => response.json())
    .then(data => console.log('Success:', data))
    .catch((error) => console.error('Error:', error));
});


const pump1OffSlider = document.getElementById('pump1-off-slider');
const pump1OffValueDisplay = document.getElementById('pump1-off-value');


document.getElementById('pump1-off-slider').addEventListener('input', function() {
    const pump1OffValue = this.value;
    document.getElementById('pump1-off-value').innerText = `${pump1OffValue} min`; // Affiche la valeur actuelle du slider

    // Envoie la nouvelle valeur au serveur
    fetch('/update-pump-interval', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ fromUser: { pump1OffValue: pump1OffValue }}),
    })
    .then(response => response.json())
    .then(data => console.log('Success:', data))
    .catch((error) => console.error('Error:', error));
});


