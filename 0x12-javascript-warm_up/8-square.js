#!/usr/bin/node
const inputArg = process.argv[2];
try {
  const size = parseInt(inputArg);
  if (isNaN(size)) {
    throw new Error('Missing size');
  }
  for (let i = 0; i < size; i++) {
    let row = '';
    for (let j = 0; j < size; j++) {
      row += 'X';
    }
    console.log(row);
  }
} catch (e) {
  console.log(e.message);
}
