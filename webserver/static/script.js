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
