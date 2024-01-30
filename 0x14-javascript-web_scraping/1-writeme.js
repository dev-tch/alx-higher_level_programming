#!/usr/bin/node
const fs = require('node:fs');
const filePath = process.argv[2];
const data = process.argv[3];
fs.writeFile(filePath, data,
  {
    encoding: 'utf8',
    flag: 'w'
  },
  (err) => {
    if (err) {
      console.error(err);
    }
  });
