#!/usr/bin/node

// check number of argument passed
const numArguments = process.argv.length - 2;

if (numArguments === 0) {
  console.log('undefined is undefined');
} else {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
}
