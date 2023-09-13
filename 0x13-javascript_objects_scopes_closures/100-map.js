#!/usr/bin/node

// Import the array from 100-data.js
const originalArray = require('./100-data.js').list;

// Use the map function to create a new array with values multiplied by their index
const newArray = originalArray.map((value, index) => value * index);

// Print both the initial list and the new list
console.log(originalArray);
console.log(newArray);
