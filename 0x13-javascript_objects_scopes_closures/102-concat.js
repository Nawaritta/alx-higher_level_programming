#!/usr/bin/node
const fs = require('fs');
const argv = process.argv;

const fileA = fs.readFileSync(argv[2], 'utf8');
const fileB = fs.readFileSync(argv[3], 'utf8');
const fileC = argv[4];
fs.writeFileSync(fileC, fileA + fileB);
