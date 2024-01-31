// Script that fetches a character from given URL

const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

fetch(url)
  .then(res => {
    if (!res.ok) throw new Error(`Sure about that URL? (${res.status})`);
    return res.json();
  })
  .then(data => {
    const characterElement = document.getElementById('character');
    let charName = data.name;
    characterElement.innerHTML = charName;
  });
