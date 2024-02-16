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
    fetch('../data.json') // Assurez-vous que le chemin vers data.json est correct
        .then(response => response.json())
        .then(data => {
            document.querySelector('.temperature .middle .left h1').innerText = `${data.temperature}°C`;
            document.querySelector('.tds .middle .left h1').innerText = `${data.tds}ppm`;
        })
}

///////////////// USER DATA /////////////////////////////
const pumpSlider = document.getElementById('pump-slider');
const pumpValueDisplay = document.getElementById('pump-value');


document.getElementById('pump-slider').addEventListener('input', function() {
    const pumpValue = this.value;
    document.getElementById('pump-value').innerText = `${pumpValue} min`; // Affiche la valeur actuelle du slider

    // Envoie la nouvelle valeur au serveur
    fetch('/update-pump-interval', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ pumpInterval: pumpValue }),
    })
    .then(response => response.json())
    .then(data => console.log('Success:', data))
    .catch((error) => console.error('Error:', error));
});