#!/usr/bin/node
const request = require('request');
const { argv } = require('process');
const api_url = 'https://swapi-api.hbtn.io/api';
const movie_id = argv[2];

request(api_url + '/films/' + movie_id, (error, response, body) => {
    error? console.error(error): console.log(JSON.parse(body).title);
});
