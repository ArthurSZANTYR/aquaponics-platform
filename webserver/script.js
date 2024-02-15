//////////////////////  ANIMATION PAGE ////////////////////////

const sideMenu = document.querySelector("aside");
const menuBtn = document.querySelector("#menu-btn");
const closeBtn = document.querySelector("#close-btn");

menuBtn.addEventListener('click', () =>{
    sideMenu.style.display = 'block';
})

closeBtn.addEventListener('click', () =>{
    sideMenu.style.display = 'none';
})

//////////////////  DATA LOAD  ////////////////////////////

document.addEventListener('DOMContentLoaded', function() {
    fetchDataAndUpdateUI();
});

function fetchDataAndUpdateUI() {
    fetch('./data.json') // Assurez-vous que le chemin vers data.json est correct
        .then(response => response.json())
        .then(data => {
            document.querySelector('.temperature .middle .left h1').innerText = `${data.temperature}°C`;
            document.querySelector('.tds .middle .left h1').innerText = `${data.tds}ppm`;
        })
}
