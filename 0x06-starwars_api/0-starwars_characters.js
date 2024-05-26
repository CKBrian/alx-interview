#!/usr/bin/node

/* Objectives:
 * - Display one character name per line in the same order as the “characters” list in the /films/ endpoint
 */

const request = require('request');
const movieId = process.argv[2];
const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/?format=json`;

/* Get Json data */
const getJson = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      }
      if (response.statusCode === 200) {
        resolve(JSON.parse(body));
      }
    });
  });
};

/* Get characters */
getJson(movieUrl)
  .then(movie => {
    const charactersUrls = movie.characters;
    const getCharacterName = characterUrl => {
      return getJson(characterUrl).then(character => character.name);
    };
    Promise.all(charactersUrls.map(getCharacterName)).then(names => names.forEach(name => console.log(name)));
  })
  .catch(error => console.error(error));
