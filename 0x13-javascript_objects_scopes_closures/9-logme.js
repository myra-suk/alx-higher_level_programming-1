#!/usr/bin/node
/*
 * Prints the number of arguments and new argument value
 */
let argvalue = 0;
exports.logMe = function (item) {
  const myprint = argvalue + ':' + item;
  console.log(myprint);
  argvalue += 1;
};
