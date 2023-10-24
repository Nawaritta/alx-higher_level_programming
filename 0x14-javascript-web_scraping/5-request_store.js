#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const requestUrl = process.argv[2];
const filepath = process.argv[3];

const writeStream = fs.createWriteStream(filepath, { encoding: 'utf8' });

request(requestUrl).pipe(writeStream);
