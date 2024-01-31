#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const filePath = process.argv[3];

function writeFile (data) {
  fs.writeFile(filePath, data, 'utf-8', err => {
    if (err) {
      console.log(err);
    }
  });
}
request(url, (error, response, body) => {
  if (error) {
    console.error('Error: ', error);
  } else {
    writeFile(body);
  }
});
