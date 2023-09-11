#!/usr/bin/node

// check number of argument passed
const numArguments = process.argv.length - 2;

if (numArguments === 0) {
  console.log('No argument');
} else if (numArguments === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
