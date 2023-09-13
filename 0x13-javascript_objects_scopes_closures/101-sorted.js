#!/usr/bin/node
const dict = require('./101-data.js').dict;

const newDict = {};

for (const uid in dict) {
  const key = dict[uid];

  if (newDict[key] === undefined) {
    newDict[key] = [uid];
  } else {
    newDict[key].push(uid);
  }
}
console.log(newDict);
