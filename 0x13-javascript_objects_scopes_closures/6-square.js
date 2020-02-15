#!/usr/bin/node
const Ssquare = require('./5-square.js');
module.exports = class Square extends Ssquare {
  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      let a = '';
      for (let i = 0; i < this.width; i++) {
        a = a + c;
      }
      for (let i = 0; i < this.width; i++) {
        console.log(a);
      }
    }
  }
};
