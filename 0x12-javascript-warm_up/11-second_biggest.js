#!/usr/bin/node
const argv = process.argv;

if (argv.length < 4) {
  console.log('0');
} else {
  let biggest = Number(argv[2]);
  let sec = Number(argv[3]);
  let i = 2;
  for (;i < argv.length; i++) {
    const x = Number(argv[i]);
    if (x > sec) {
      if (x > biggest) { sec = biggest; biggest = x; } else if (x < biggest) { sec = x; }
    }
  }
  console.log(sec);
}
