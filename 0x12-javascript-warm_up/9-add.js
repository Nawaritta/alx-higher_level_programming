#!/usr/bin/node
const { argv } = require('process');
function add (a, b) {
  return a + b;
}

console.log(add(Number(argv[2]), Number(argv[3])));
