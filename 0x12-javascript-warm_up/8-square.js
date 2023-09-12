#!/usr/bin/node
const argv = process.argv;
const x = argv[2];
if (isNaN(x)) {
  console.log('Missing size');
} else {
  let i = x;
  while (i > 0) {
    console.log('X'.repeat(x));
    i--;
  }
}
