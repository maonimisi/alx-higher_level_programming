// JavaScript script that fetches and lists the title for all movies by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json

const $ = window.$;
const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

$(function () {
  $.get(url, function (data, statusText) {
    if (statusText === 'successs') {
      const films = data.results;
      for (const i in films) {
        $('#list_movies').append('<li>' + films[i].title + '</li>');
      }
    }
  });
});
