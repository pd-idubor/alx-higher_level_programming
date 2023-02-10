#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request(url, function (error, response, body) {
  if (error) {
    return;
  }

  const retDict = {};
  const result = JSON.parse(body);

  for (let i = 0; i < result.length; i++) {
    if (result[i].completed === true) {
      if (retDict[result[i].userId] === undefined) {
        retDict[result[i].userId] = 1;
      } else {
        retDict[result[i].userId] += 1;
      }
    }
  }
  console.log(retDict);
});
