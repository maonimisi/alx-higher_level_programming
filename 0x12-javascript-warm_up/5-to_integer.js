#!/usr/bin/node

// check if first argument can be converted to an integer
const firstArg = Math.floor(Number(process.argv[2]));

if (Number.isNaN(Number(firstArg))) {
  console.log('Not a number');
} else {
  console.log(`My number: ${firstArg}`);
}
