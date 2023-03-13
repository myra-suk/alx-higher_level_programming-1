#!/usr/bin/node
/*
 * Prints two arguments passed to it in a given format
 */
const argc = process.argv;
const myString = argc[2] + ' is ' + argc[3];
console.log(myString);
