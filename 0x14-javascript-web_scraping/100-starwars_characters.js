#!/usr/bin/node
const request = require('request');
const { argv } = require('process');
const movieId = argv[2];
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request.get(apiUrl, (error, response, body) => {
  if (!error) {
    const data = JSON.parse(body);
    const charactersList = data.characters;
    for (const character of charactersList) {
      request(character, (error, response, body) => {
        if (!error) {
          const characterInfo = JSON.parse(body);
          console.log(characterInfo.name);
        } else {
          console.log(error);
        }
      });
    }
  } else {
    console.log(error);
  }
});
