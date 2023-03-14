#!/usr/node/bin
/*
 * Returns the number of occurences in a list
 */
exports.nbOccurences = function (list, searchElement) {
  let occurence = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      occurence += 1;
    }
  }
  return (occurence);
};
