#!/usr/bin/node
const request = require('request');
const { argv } = require('process');
const apiUrl = 'https://swapi-api.hbtn.io/api';
const movieId = argv[2];

request(apiUrl + '/films/' + movieId, (error, response, body) => {
  error ? console.error(error) : console.log(JSON.parse(body).title);
});
