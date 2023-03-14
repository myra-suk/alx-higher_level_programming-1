#!/usr/bin/node
/*
 * Returns the reversed version of a list
 */
exports.esrever = function (list) {
  const listb = list.slice();
  for (let i = 0; i < list.length; i++) {
    list[i] = listb[list.length - i - 1];
  }
  return list;
};
