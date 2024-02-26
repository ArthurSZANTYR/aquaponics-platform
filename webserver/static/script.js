//////////////////////  ANIMATION PAGE ////////////////////////

const sideMenu = document.querySelector("aside");
const menuBtn = document.querySelector("#menu-btn");
const closeBtn = document.querySelector("#close-btn");
const pumpBtn = document.querySelector("#pump-btn"); 
const ledBtn = document.querySelector("#led-btn"); 
const led2Btn = document.querySelector("#led2-btn"); 

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

ledBtn.addEventListener('click', () => {
    window.location.href = 'led1.html'; 
});

led2Btn.addEventListener('click', () => {
    window.location.href = 'led2.html'; 
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

if(pump1OnSlider != null) {
    pump1OnSlider.addEventListener('input', function() {
        const pump1OnValue = this.value;
        pump1OnValueDisplay.innerText = `${pump1OnValue} min`; // Affiche la valeur actuelle du slider
    
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
}




const pump1OffSlider = document.getElementById('pump1-off-slider');
const pump1OffValueDisplay = document.getElementById('pump1-off-value');

if(pump1OffSlider != null) {
pump1OffSlider.addEventListener('input', function() {
    const pump1OffValue = this.value;
    pump1OffValueDisplay.innerText = `${pump1OffValue} min`; // Affiche la valeur actuelle du slider

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
}

const led1IntensitySlider = document.getElementById('led1-intensity-slider');
const led1IntensityValueDisplay = document.getElementById('led1-intensity-value');

if(led1IntensitySlider != null) {
led1IntensitySlider.addEventListener('input', function() {
    const led1IntensityValue = this.value;
    led1IntensityValueDisplay.innerText = led1IntensityValue; // Affiche la valeur actuelle du slider

    // Envoie la nouvelle valeur au serveur
    fetch('/update-led-interval', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ fromUser: { led1IntensityValue: led1IntensityValue }}),
    })
    .then(response => response.json())
    .then(data => console.log('Success:', data))
    .catch((error) => console.error('Error:', error));
});

}

const led2IntensitySlider = document.getElementById('led2-intensity-slider');
const led2IntensityValueDisplay = document.getElementById('led2-intensity-value');

if(led2IntensitySlider != null) {
led2IntensitySlider.addEventListener('input', function() {
    const led2IntensityValue = this.value;
    led2IntensityValueDisplay.innerText = led2IntensityValue; // Affiche la valeur actuelle du slider

    // Envoie la nouvelle valeur au serveur
    fetch('/update-led-interval', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ fromUser: { led2IntensityValue: led2IntensityValue }}),
    })
    .then(response => response.json())
    .then(data => console.log('Success:', data))
    .catch((error) => console.error('Error:', error));
});

}

const led1OnSlider = document.getElementById('led1-ON-slider');
const led1OnValueDisplay = document.getElementById('led1-ON-value');

if(led1OnSlider != null) {
    led1OnSlider.addEventListener('input', function() {
    const led1OnValue = this.value;
    led1OnValueDisplay.innerText = led1OnValue; // Affiche la valeur actuelle du slider

    // Envoie la nouvelle valeur au serveur
    fetch('/update-led-interval', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ fromUser: { led1OnValue: led1OnValue }}),
    })
    .then(response => response.json())
    .then(data => console.log('Success:', data))
    .catch((error) => console.error('Error:', error));
});

}

const led2OnSlider = document.getElementById('led2-ON-slider');
const led2OnValueDisplay = document.getElementById('led2-ON-value');

if(led2OnSlider != null) {
    led2OnSlider.addEventListener('input', function() {
    const led2OnValue = this.value;
    led2OnValueDisplay.innerText = led2OnValue; // Affiche la valeur actuelle du slider

    // Envoie la nouvelle valeur au serveur
    fetch('/update-led-interval', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ fromUser: { led2OnValue: led2OnValue }}),
    })
    .then(response => response.json())
    .then(data => console.log('Success:', data))
    .catch((error) => console.error('Error:', error));
});

}





