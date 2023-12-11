#!/usr/bin/node
function factorial (n) {
  if (n === 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

const inputArg = process.argv[2];
const number = parseInt(inputArg);
if (!isNaN(number)) {
  console.log(factorial(number));
} else {
  console.log('1');
}
