#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let occ = 0;
  let i = 0;

  for (; i < list.length; i++) {
    if (list[i] === searchElement) { occ++; }
  }

  return occ;
};
