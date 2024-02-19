document.addEventListener("DOMContentLoaded", function() {
    fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
        .then(response => response.json())
        .then(data => {
            document.getElementById('hello').innerText = data.hello;
        })
        .catch(error => console.error('Error al obtener la traducción:', error));
});
