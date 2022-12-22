#!/usr/bin/node

const num = process.argv[2];

function func (n) {
  if (num === undefined) {
    return 1;
  } else if (n === 0) {
    return (1);
  } else {
    return (n * func(n - 1));
  }
}
console.log(func(num));
