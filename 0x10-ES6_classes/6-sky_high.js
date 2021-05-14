import Building from './5-building';

export default class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    super(sqft);
    this._floors = floors;
  }

  // getter
  get sqft() {
    return this._sqft;
  }

  get floors() {
    return this._floors;
  }

  // setter
  set sqft(sqft) {
    this._sqft = sqft;
  }

  set floors(floors) {
    this._floors = floors;
  }

  evacuationWarningMessage() {
    return `Evacuate slowly the ${this._floors} floors`;
  }
}
