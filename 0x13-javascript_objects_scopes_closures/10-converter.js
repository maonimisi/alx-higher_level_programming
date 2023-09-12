#!/usr/bin/node

// function that converts a number from base 10 to another base passed as argument
exports.converter = function (base) {
  return function convertToBase (num) {
    if (num < base) {
      return num.toString();
    } else {
      return convertToBase(Math.floor(num / base)) + (num % base).toString();
    }
  };
};
