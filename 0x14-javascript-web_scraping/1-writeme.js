#!/usr/bin/node
const fs = require('fs');
const filepath = process.argv[2];
const filecontent = process.argv[3];

fs.writeFile(filepath, filecontent, 'utf-8', function (error) {
  if (error) { console.error(error); }
});
