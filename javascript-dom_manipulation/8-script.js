// Script that fetches and displays hello from given url in #hello

const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

fetch(url)
  .then(res => {
    if (!res.ok) throw new Error(res.status);
    return res.json();
  })
  .then(data => {
    const helloElement = document.getElementById('hello');
    helloElement.innerHTML();
  });
