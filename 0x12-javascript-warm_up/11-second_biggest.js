#!/usr/bin/node

const argArr = process.argv;
function func (arr) {
  if (arr[2] === undefined || arr.length === 3) {
    return (0);
  }

  let m = arr[2];
  let n = arr[3];

  for (let i = 2; i < arr.length; i++) {
    if (m < arr[i]) {
      n = m;
      m = arr[i];
    } else if (arr[i] > n && arr[i] < m) {
      n = arr[i];
    }
  }
  return (n);
}
console.log(func(argArr));
