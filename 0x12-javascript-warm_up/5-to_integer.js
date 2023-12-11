#!/usr/bin/node

const castedNumber = parseInt(process.argv[2]);
if (!isNaN(castedNumber)) {
  console.log(`My number: ${castedNumber}`);
} else {
  console.log('Not a number');
}
