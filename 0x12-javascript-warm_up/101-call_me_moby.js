#!/usr/bin/node
// callMeMoby.js
exports.callMeMoby = function (x, theFunction) {
  const rep = eval(theFunction);
  for (let i = 0; i < x; i++) {
    rep();
  }
};
