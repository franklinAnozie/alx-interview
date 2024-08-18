#!/usr/bin/node

const request = require('request');
const process = require('process');

const makeRequest = (url) => {
  return new Promise((resolve, reject) => {
    request({
      uri: url,
      json: true
    }, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(body);
      }
    });
  });
};

const getMovieCharacters = async (URL) => {
  try {
    const movieData = await makeRequest(URL);
    const charactersURLArray = movieData.characters;
    const characterPromises = charactersURLArray.map(url => makeRequest(url));
    const characters = await Promise.all(characterPromises);
    characters.forEach(character => {
      console.log(character.name);
    });
  } catch (error) {
    console.log('Error:', error.message);
  }
};

if (process.argv.length !== 3) {
  console.log('Usage: node script.js <movie_id>');
  process.exit(1);
} else {
  const id = process.argv[2];
  const URI = `https://swapi-api.alx-tools.com/api/films/${id}`;
  getMovieCharacters(URI);
}
