#!/usr/bin/node
// this script reads and prints the content of a file

const fs = require('fs');
const fileName = process.argv[2];

fs.readFile(fileName, 'utf-8', function (error, data) {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
