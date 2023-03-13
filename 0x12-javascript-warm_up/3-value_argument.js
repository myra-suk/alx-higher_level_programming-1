#!/usr/bin/node
/*
 * Prints the first argument passed to it.
 */
const argc = process.argv;
if (argc[2]) {
  console.log(argc[2]);
} else {
  console.log('No argument');
}
