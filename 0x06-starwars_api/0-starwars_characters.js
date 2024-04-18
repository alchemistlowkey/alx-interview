#!/usr/bin/node

const util = require('util');
const request = util.promisify(require('request'));

const movieId = process.argv[2];

async function fetchMovieCharacters (movieId) {
  const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

  try {
    const response = await (await request(movieUrl));
    const movieData = JSON.parse(response.body);
    const characters = movieData.characters;

    for (const characterUrl of characters) {
      const characterResponse = await (await request(characterUrl));
      const characterData = JSON.parse(characterResponse.body);
      console.log(characterData.name);
    }
  } catch (error) {
    console.error('Error:', error.message);
  }
}

fetchMovieCharacters(movieId);
