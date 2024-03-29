import Car from './10-car';

export default class EVCar extends Car {
  constructor(brand, motor, color, range) {
    super(brand, motor, color);
    this._range = range;
  }

  static get [Symbol.species]() {
    return Car;
  }

  cloneCar() {
    const Species = this.constructor[Symbol.species];
    const { this: _brand, this: _motor, this: _color } = this;
    const object = new Species(_brand, _motor, _color);
    return object;
  }
}
