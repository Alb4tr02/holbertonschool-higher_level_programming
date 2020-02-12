#!/usr/bin/node
const request = require('request');
if (process.argv[2] !== undefined) {
  request(process.argv[2], function (error, response, body) {
    if (error) { console.log(error); } else {
      const cnt = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
      const res = JSON.parse(body);
      for (const dic of res) {
        const pos = dic.userId - 1;
        if (dic.completed) { cnt[pos] += 1; }
      }
      let msg = '{ ';
      let sep = '';
      for (let i = 0; i < cnt.length; i++, sep = ',\n  ') {
        msg += sep + '\'' + (i + 1) + '\': ' + cnt[i];
      }
      process.stdout.write(msg + ' }\n');
    }
  });
}
