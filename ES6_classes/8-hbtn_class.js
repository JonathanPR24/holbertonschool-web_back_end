// 8-hbtn_class.js

export default class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  get size() {
    return this._size;
  }

  get location() {
    return this._location;
  }

  valueOf() {
    return this._size; // Casting to a Number returns the size
  }

  toString() {
    return this._location; // Casting to a String returns the location
  }
}
