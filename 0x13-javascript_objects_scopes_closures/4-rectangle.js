#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // methods
  print () {
    let a = '';
    for (let i = 0; i < this.width; i++) {
      a = a + 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(a);
    }
  }

  rotate () {
    const a = this.width;
    this.width = this.height;
    this.height = a;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
