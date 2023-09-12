#!/usr/bin/node
const argv = process.argv;

if (argv.length < 4) {
  console.log('0');
} else {
  let biggest = Number(argv[2]);
  let sec = Number(argv[3]);
  let i = 3;
  for (;i < argv.length; i++) {
    if (Number(argv[i]) > biggest) {
      sec = biggest;
      biggest = Number(argv[i]);
    }
  }
  console.log(sec);
}
