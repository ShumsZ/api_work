// app.js
document.addEventListener('DOMContentLoaded', () => {
    fetchMovies();
});

// function to access the /movies endpoint to get the list of all movies
async function fetchMovies() {
    const response = await fetch('/movies');
    const data = await response.json();

    // call the displayMovies function detailed below to render the list
    displayMovies(data.movies);
}

// loops through each of the movies in the list
function displayMovies(movies) {
    const moviesContainer = document.getElementById('movies-container');

    movies.forEach(movie => {
        const movieCard = document.createElement('div');
        movieCard.classList.add('movie-card');
        movieCard.innerHTML = `
            <h3>${movie.title}</h3>
            <p>Genre: ${movie.genre}</p>
            <p>Would Watch Again: ${movie.would_watch_again}</p>
        `;
        moviesContainer.appendChild(movieCard);
    });
}