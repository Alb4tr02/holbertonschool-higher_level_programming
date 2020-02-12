#!/usr/bin/node
const request = require('request');
if (process.argv[2] !== undefined) {
  request(process.argv[2], function (error, response, body) {
    if (error) { console.log(error); } else {
      const cnt = {};
      const res = JSON.parse(body);
      for (const dic of res) {
        const k = dic.userId;
        if (dic.completed) {
          if (!(k in cnt)) cnt[k] = 1;
          else cnt[k]++;
        }
      }
      console.log(cnt);
    }
  });
}
