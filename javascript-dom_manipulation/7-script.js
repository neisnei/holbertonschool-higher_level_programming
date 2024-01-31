// Script that fetches and lists all movies by given url

const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

fetch(url)
  .then(res => {
    if (!res.ok) throw new Error(res.status);
    return res.json();
  })
  .then(data => {
    const movies = data.results;
    const listMovies = document.getElementById('list_movies');

    movies.map(movie => {
      const movieElement = document.createElement('li');
      movieElement.innerHTML = movie.title;
      listMovies.appendChild(movieElement);
    });
  });
