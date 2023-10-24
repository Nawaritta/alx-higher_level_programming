#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const request_url = process.argv[2];
const filepath = process.argv[3];

const writeStream = fs.createWriteStream(filepath, { encoding: 'utf8' });

request(request_url).pipe(writeStream);
