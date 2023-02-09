#!/usr/bin/node

const id = process.argv[2];
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, function (error, response, body) {
  if (error) {
    return;
  }
  console.log(JSON.parse(body).title);
});
