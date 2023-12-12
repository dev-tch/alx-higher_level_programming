#!/usr/bin/node
function comparator (a, b) {
  return b - a;
}

const len = process.argv.length;
if (len <= 3) {
  console.log('0');
} else {
  const newArray = process.argv.slice(2, len);
  newArray.sort(comparator);
  console.log(newArray[1]);
}
