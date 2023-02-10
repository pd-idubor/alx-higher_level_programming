#!/usr/bin/node

const url = process.argv[2];
const path = process.argv[3];
const request = require('request');

request(url, function (error, response, body) {
  if (!error) {
    const fs = require('fs');
    fs.writeFile(path, body, 'utf-8', function (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});
