#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request(url, function (error, response, body) {
  if (error) {
    return;
  }

  let count = 0;
  const films = JSON.parse(body).results;
  for (let i = 0; i < films.length; i++) {
    const chars = films[i].characters;
    for (let j = 0; j < chars.length; j++) {
      if (chars[j].includes('/18/')) {
        count += 1;
      }
    }
  }
  console.log(count);
});
