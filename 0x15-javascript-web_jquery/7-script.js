// JavaScript script that fetches the character name from this URL: https://swapi-api.alx-tools.com/api/people/5/?format=json
const $ = window.$;
const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

$(function () {
  $.get(url, function (data, statusText) {
    if (statusText === 'success') {
      $('#character').text(data.name);
    }
  });
});
