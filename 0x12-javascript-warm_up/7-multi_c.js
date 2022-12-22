#!/usr/bin/node

const num = process.argv[2];
if (parseInt(num)) {
  for (let i = 0; i < parseInt(num); i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
