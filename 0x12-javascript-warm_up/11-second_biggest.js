#!/usr/bin/node

// Script that searches the second biggest integer in the list of arguments

const args = process.argv.slice(2);

if (args.length <= 1) {
  console.log(0);
} else {
  const integers = args.map(Number).filter(Number.isInteger);
  integers.sort((a, b) => b - a);

  if (integers.length < 2) {
    console.log(0);
  } else {
    console.log(integers[1]);
  }
}
