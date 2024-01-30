#!/usr/bin/node
const request = require('request');
const apiFilm = 'https://swapi-api.alx-tools.com/api/films/';
const url = apiFilm + process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.error('Error: ', error);
  } else {
    const jsonObject = JSON.parse(body);
    console.log(jsonObject.title);
  }
});
