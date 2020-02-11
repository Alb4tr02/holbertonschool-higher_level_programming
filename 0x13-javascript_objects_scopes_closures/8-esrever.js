#!/usr/bin/node
exports.esrever = function (list) {
  const n = [];
  list.forEach(elmnt => n.unshift(elmnt));
  return n;
};
