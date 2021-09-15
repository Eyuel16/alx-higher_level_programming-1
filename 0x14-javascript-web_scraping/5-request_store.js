#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const filename = process.argv[3];

request(process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(filename, body, 'utf8', function (err, response, body) {
      if (err) {
        console.log(err);
      }
    });
  }
});
