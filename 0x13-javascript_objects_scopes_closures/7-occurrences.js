#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let n = 0;
  list.forEach(function (elmnt) {
    if (elmnt === searchElement) {
      n = n + 1;
    }
  });
  return n;
};
