#!/usr/bin/node
const inputArg = process.argv[2];
try {
  const times = parseInt(inputArg);
  if (isNaN(times)) {
    throw new Error('Missing number of occurrences');
  }
  /* loop times */
  for (let i = 0; i < times; i++) {
    console.log('C is fun');
  }
} catch (e) {
  console.log(e.message);
}
