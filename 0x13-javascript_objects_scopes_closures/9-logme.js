#!/usr/bin/node
/*
 * Prints the number of arguments and new argument value
 */
exports.logMe = function (item) {
  const myprint = argvalue + ': ' + item;
  console.log(myprint);
  argvalue += 1;
};
let argvalue = 0;
