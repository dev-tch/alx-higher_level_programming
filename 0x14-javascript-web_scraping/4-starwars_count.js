#!/usr/bin/node
const request = require('request');
const apiFilm = 'https://swapi-api.alx-tools.com/api/films/';
let total = 0;
request(apiFilm, (error, response, body) => {
  if (error) {
    console.error('Error: ', error);
  } else {
    const jsonObject = JSON.parse(body);
    const objArray = jsonObject.results;
    objArray.forEach(function (itemJson) {
      const arrayChar = itemJson.characters;
      let index = 0;
      index = arrayChar.findIndex(value => /18/.test(value));
      if (index > 0) {
        total = total + 1;
      }
    });
    console.log(total);
  }
});
