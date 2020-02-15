#!/usr/bin/node

const n = Number(process.argv[2]);
let x = '';
if (isNaN(n)) {
  console.log('Missing size');
} else {
  for (let j = 0; j < n; j++) {
    x = x + 'X';
  }
  for (let i = 0; i < n; i++) {
    console.log(x);
  }
}
