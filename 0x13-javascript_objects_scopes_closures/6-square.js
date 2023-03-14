#!/usr/bin/node
/*
 * A square class that inherits from the class Rectangle
 */
const prevsquare = require('./5-square');
class Square extends prevsquare {
  // Prints the rectangle using the character C
  charPrint (c = 'X') {
    let sqr = '';
    for (let i = 0; i < this.width; i++) {
      sqr += c;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(sqr);
    }
  }
}
module.exports = Square;
