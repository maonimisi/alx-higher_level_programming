#!/usr/bin/node
// script that prints x times “C is fun”

// check if first argument can be converted to an integer
const firstArg = Math.floor(Number(process.argv[2]));

if (Number.isNaN(Number(firstArg))) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < firstArg; i++) {
    console.log('C is fun');
  }
}
