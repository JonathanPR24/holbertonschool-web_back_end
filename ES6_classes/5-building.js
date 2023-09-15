/* eslint-disable */
export default class Building {
    constructor(sqft) {
      if (
        Object.getPrototypeOf(this) !== Building.prototype
        && typeof this.evacuationWarningMessage !== 'function'
      ) {
        throw Error(
          'Class extending Building must override evacuationWarningMessage',
        );
      }
  
      this._sqft = sqft;
    }
  
    get sqft() {
      return this._sqft;
    }
  }
