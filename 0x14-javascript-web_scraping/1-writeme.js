#!/usr/bin/node
// script that writes a string to a file

const fs = require('fs');
const oldFileName = process.argv[2];
const newFileName = process.argv[3];

request.writeFile(oldFileName, newFileName, 'utf-8', function (error) {
  if (error) {
    console.log(error);
  }
});
