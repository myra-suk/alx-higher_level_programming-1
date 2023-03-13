#!/usr/bin/node
/*
 * Prints a Square
 */
const sqr = 'X';
const argc = process.argv;
const num = Number(argc[2]);
if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    let myString = '';
    for (let j = 0; j < num; j++) myString += sqr;
    console.log(myString);
  }
}
