#!/usr/bin/node

const one = process.argv[2];
if (parseInt(one)) {
  console.log('My number:', parseInt(one));
} else {
  console.log('Not a number');
}
