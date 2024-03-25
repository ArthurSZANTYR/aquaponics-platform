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
const pump1OnSlider = document.getElementById('pump1-on-slider');
const pump1OffSlider = document.getElementById('pump1-off-slider');
const pump1OnValueDisplay = document.getElementById('pump1-on-value');
const pump1OffValueDisplay = document.getElementById('pump1-off-value');

const led1IntensitySlider = document.getElementById('led1-intensity-slider');
const led1OnSlider = document.getElementById('led1-ON-slider');
const led1StartSlider = document.getElementById('led1-start-slider');
const led1IntensityValueDisplay = document.getElementById('led1-intensity-value');
const led1OnValueDisplay = document.getElementById('led1-ON-value');
const led1StartValueDisplay = document.getElementById('led1-start-value');

const led2IntensitySlider = document.getElementById('led2-intensity-slider');
const led2OnSlider = document.getElementById('led2-ON-slider');
const led2StartSlider = document.getElementById('led2-start-slider');
const led2IntensityValueDisplay = document.getElementById('led2-intensity-value');
const led2OnValueDisplay = document.getElementById('led2-ON-value');
const led2StartValueDisplay = document.getElementById('led2-start-value');

const temperatureValueDisplay = document.getElementById('temperature-value');
const tdsValueDisplay = document.getElementById('tds-value');

document.addEventListener('DOMContentLoaded', function() {
    fetchDataAndUpdateUI();
    setInterval(fetchDataAndUpdateUI, 5000); // Rafraîchit les données toutes les 5 secondes
});

function fetchDataAndUpdateUI() {
    fetch('../data.json') 
        .then(response => response.json())
        .then(data => {

            if(temperatureValueDisplay != null){
            // Mise à jour de l'interface utilisateur avec les nouvelles valeurs
            const fromSystem = data.fromSystem || {}; // Fournit un objet vide par défaut
            const temperature = fromSystem.temperature || 'N/A'; // Utilise 'N/A' comme valeur par défaut
            const tds = fromSystem.tds || 'N/A';

            temperatureValueDisplay.innerText = `${temperature}°C`;
            tdsValueDisplay.innerText = `${tds}ppm`;
            }
            
            const fromUser = data.fromUser || {};
            if(pump1OnValueDisplay != null) {
                const pump1OnValue = fromUser.pump1OnValue || 'N/A';
                pump1OnSlider.value = pump1OnValue;
                pump1OnValueDisplay.innerText = `${pump1OnValue} min`;

                const pump1OffValue = fromUser.pump1OffValue || 'N/A';
                pump1OffSlider.value = pump1OffValue;
                pump1OffValueDisplay.innerText = `${pump1OffValue} min`;
            }

            if(led1IntensityValueDisplay != null) {
                const led1IntensityValue = fromUser.led1IntensityValue || 'N/A';
                led1IntensitySlider.value = led1IntensityValue;
                led1IntensityValueDisplay.innerText = `${led1IntensityValue}`;

                const led1OnValue = fromUser.led1OnValue || 'N/A';
                led1OnSlider.value = led1OnValue;
                led1OnValueDisplay.innerText = `${led1OnValue}`;

                const led1StartValue = fromUser.led1StartValue || 'N/A';
                led1StartSlider.value = led1StartValue;
                led1StartValueDisplay.innerText = `${led1StartValue}`;
            }

            if(led2IntensityValueDisplay != null) {
                const led2IntensityValue = fromUser.led2IntensityValue || 'N/A';
                led2IntensitySlider.value = led2IntensityValue;
                led2IntensityValueDisplay.innerText = `${led2IntensityValue}`;

                const led2OnValue = fromUser.led2OnValue || 'N/A';
                led2OnSlider.value = led2OnValue;
                led2OnValueDisplay.innerText = `${led2OnValue}`;

                const led2StartValue = fromUser.led2StartValue || 'N/A';
                led2StartSlider.value = led2StartValue;
                led2StartValueDisplay.innerText = `${led2StartValue}`;
            }

        })
        .catch(error => console.error('Error fetching data:', error)); // Gestion des erreurs
}

///////////////// USER DATA /////////////////////////////
//const pump1OnSlider = document.getElementById('pump1-on-slider');
//const pump1OnValueDisplay = document.getElementById('pump1-on-value');

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


if(led1StartSlider != null) {
    led1StartSlider.addEventListener('input', function() {
    const led1StartValue = this.value;
    led1StartValueDisplay.innerText = led1StartValue; // Affiche la valeur actuelle du slider

    // Envoie la nouvelle valeur au serveur
    fetch('/update-led-interval', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ fromUser: { led1StartValue: led1StartValue }}),
    })
    .then(response => response.json())
    .then(data => console.log('Success:', data))
    .catch((error) => console.error('Error:', error));
});

}

if(led2StartSlider != null) {
    led2StartSlider.addEventListener('input', function() {
    const led2StartValue = this.value;
    led2StartValueDisplay.innerText = led2StartValue; // Affiche la valeur actuelle du slider

    // Envoie la nouvelle valeur au serveur
    fetch('/update-led-interval', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ fromUser: { led2StartValue: led2StartValue }}),
    })
    .then(response => response.json())
    .then(data => console.log('Success:', data))
    .catch((error) => console.error('Error:', error));
});

}

