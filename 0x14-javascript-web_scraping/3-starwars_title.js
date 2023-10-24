#!/usr/bin/node
// script that prints the title of a Star Wars movie where the episode number matches a given integer

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/:id';
const movieID = process.argv[2];

request(url + movieID, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const json = JSON.parse(body);
  console.log(json.title);
});
