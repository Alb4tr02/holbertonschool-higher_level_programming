#!/usr/bin/node

let first = Number(process.argv[2]);
let second = Number(process.argv[3]);
if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(0);
} else {
  for (let i = 2; i < process.argv.length; i++) {
    if (Number(process.argv[i]) > first) {
      second = first;
      first = Number(process.argv[i]);
    }
  }
  console.log(second);
}
