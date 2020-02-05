#!/usr/bin/node
/* eslint-disable no-eval */
// callMeMoby.js
exports.callMeMoby = function (x, theFunction) {
  const rep = eval(theFunction);
  for (let i = 0; i < x; i++) {
    rep();
  }
};
