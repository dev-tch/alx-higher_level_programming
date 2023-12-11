#!/usr/bin/node
function add (a, b) {
  return a + b;
}
const inputArg1 = process.argv[2];
const inputArg2 = process.argv[3];

const number1 = parseInt(inputArg1);
const number2 = parseInt(inputArg2);
if (!isNaN(number1) && !isNaN(number2)) {
  console.log(add(number1, number2));
} else {
  console.log('NaN');
}
