#!/usr/bin/node
/*
 * Defines a Rectangle
 * Prints the rectangle
 */
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // Method to print the Rectangle
  print () {
    let rect = '';
    for (let i = 0; i < this.width; i++) {
      rect += 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(rect);
    }
  }
}
module.exports = Rectangle;
