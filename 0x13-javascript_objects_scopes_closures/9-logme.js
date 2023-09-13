#!/usr/bin/node

let printed = 0;

exports.logMe = function count (item) {
  console.log(printed + ': ' + item);
  printed++;
};
