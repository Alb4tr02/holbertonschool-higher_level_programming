#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  const res = JSON.parse(body).results;
  const cmp = 'https://swapi.co/api/people/18/';
  let cnt = 0;
  res.forEach(function (elmnt) {
    if (elmnt.characters.includes(cmp)) cnt++;
  });
  console.log(cnt);
  if (error) {}
});
