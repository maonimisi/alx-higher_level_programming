#!/usr/bin/node
// Import the dictionary of occurrences from 101-data.js
const occurrencesDict = require('./101-data.js').dict;

// Initialize an empty dictionary for user IDs by occurrence
const userIDsByOccurrence = {};

// Iterate over the entries in the occurrencesDict
for (const userID in occurrencesDict) {
  const occurrenceCount = occurrencesDict[userID];

  // If the occurrence count is not already a key in userIDsByOccurrence, initialize it as an empty array
  if (!userIDsByOccurrence[occurrenceCount]) {
    userIDsByOccurrence[occurrenceCount] = [];
  }

  // Push the user ID into the corresponding occurrence count array
  userIDsByOccurrence[occurrenceCount].push(userID);
}

// Print the new dictionary
console.log(userIDsByOccurrence);
