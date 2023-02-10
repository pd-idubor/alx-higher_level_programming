#!/usr/bin/node

const id = process.argv[2];
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, function (error, response, body) {
  if (error) {
    return;
  }
  const result = JSON.parse(body);
  const chars = result.characters;
  for (let i = 0; i < chars.length; i++) {
    request(chars[i], function (eror, response, body) {
      if (!error) {
        console.log(JSON.parse(body).name);
      }
    });
  }
});
