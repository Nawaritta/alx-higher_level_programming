#!/usr/bin/node
const argv = process.argv;

if (argv.length < 4) {
  console.log('0');
} else {
  let biggest = Number(argv[2]);
  let i = 2;
  for (;i < argv.length; i++) { if (Number(argv[i]) > biggest) { biggest = Number(argv[i]); } }
  i = 2;
  let sec = Number(argv[2]) === biggest ? Number(argv[3]) : Number(argv[2]);
  for (;i < argv.length; i++) { if (Number(argv[i]) > sec && Number(argv[i]) !== biggest) { sec = Number(argv[i]); } }

  console.log(sec);
}
