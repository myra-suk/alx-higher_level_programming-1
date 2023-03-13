#!/usr/bin/node
/*
 * Prints X times "C is Fun"
 */
const argc = process.argv;
const x = Number(argc[2]);
const myString = 'C is fun';
if (isNaN(x)) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < x; i++) {
    console.log(myString);
  }
}
