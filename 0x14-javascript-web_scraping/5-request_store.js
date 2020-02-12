#!/usr/bin/node
const request = require('request');
const wr = require('fs');
if (process.argv[2] !== undefined) {
  request(process.argv[2], function (error, response, body) {
    if (error) { console.log(error); } else {
      wr.writeFile(process.argv[3], body, (err) => {
        if (err) console.log(err);
      });
    }
  });
}
