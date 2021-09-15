#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
request('https://swapi-api.hbtn.io/api/films/' + id + '/', function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    body = JSON.parse(body);
    console.log(body.title);
  } else {
    console.log('Erorr Code:' + response.statusCode);
  }
});
