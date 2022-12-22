#!/usr/bin/node

const num = parseInt(process.argv[2]);
const sym = 'X';
if (num) {
  for (let i = 0; i < num; i++) {
    console.log(sym.repeat(num));
  }
} else {
  console.log('Missing size');
}
