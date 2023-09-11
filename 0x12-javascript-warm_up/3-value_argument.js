#!/usr/bin/node

// check number of argument passed
const numArguments = process.argv.length - 2;

if (numArguments === 0) {
  console.log('No Argument');
} else if (numArguments >= 1) {
  console.log(process.argv[2]);
}
