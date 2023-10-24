#!/usr/bin/node
const request = require('request');
const { argv } = require('process');
const apiUrl = argv[2];
const characterId = 18;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const films = JSON.parse(body).results;
  const numberOfMovies = films.reduce((count, film) => {
    if (film.characters.find(characterUrl => characterUrl.endsWith(characterId + '/'))) {
      return count + 1;
    }
    return count;
  }, 0);
  console.log(numberOfMovies);
});
