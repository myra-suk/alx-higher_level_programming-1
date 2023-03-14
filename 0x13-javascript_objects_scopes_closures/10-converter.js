#!/usr/bin/node
/*
 * Converts a number from base 10
 */
exports.converter = function (base) {
  return function innerFunction (inner) {
    return parseInt(inner).toString(base);
  };
};
