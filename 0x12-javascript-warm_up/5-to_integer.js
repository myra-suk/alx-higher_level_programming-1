#!/usr/bin/node
/*
 * Prints  My number: <first argument converted in integer>
 */
const argc = process.argv;
const num = Number(argc[2]);
if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + num);
}
