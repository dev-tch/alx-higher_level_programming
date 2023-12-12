#!/usr/bin/node
let nbargs = 0;
exports.logMe = function (item) {
  console.log(`${nbargs}: ${item}`);
  nbargs++;
};
