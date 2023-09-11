#!/usr/bin/node

// script that prints a square

// check if first argument can be converted to an integer
const firstArg = Math.floor(Number(process.argv[2]));

if (Number.isNaN(Number(firstArg))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < firstArg; i++) {
    console.log('X'.repeat(firstArg));
  }
}
