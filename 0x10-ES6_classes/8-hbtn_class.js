export default class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  [Symbol.toPrimitive](val) {
    return (val === 'number' ? this._size : this._location);
  }
}
