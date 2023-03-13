#!/usr/bin/node
/*
 * Computes and prints a factorial
 */
const argc = process.argv;
const num = Number(argc[2]);
function factorial (n) {
  if (isNaN(n) || n < 1) {
    return (1);
  }
  return (n * factorial(n - 1));
}
console.log(factorial(num));
