#!/usr/bin/node
const request = require('request');
const { argv } = require('process');
const movieId = argv[2];
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (!error) {
    const data = JSON.parse(body);
    const charactersList = data.characters;
    const characterRequests = charactersList.map((characterUrl) => {
      return new Promise((resolve, reject) => {
        request.get(characterUrl, (error, response, body) => {
          if (!error) {
            const characterInfo = JSON.parse(body);
            resolve(characterInfo.name);
          } else {
            reject(error);
          }
        });
      });
    });

    Promise.all(characterRequests).then((characterNames) => {
      characterNames.forEach((characterName) => {
        console.log(characterName);
      });
    })
      .catch((error) => {
        console.log(error);
      });
  } else {
    console.log(error);
  }
});
