#!/usr/bin/node
/*
 * Prints the addition of two integers
 */
const argc = process.argv;
const num1 = Number(argc[2]);
const num2 = Number(argc[3]);
function add (a, b) {
  return a + b;
}
console.log(add(num1, num2));
