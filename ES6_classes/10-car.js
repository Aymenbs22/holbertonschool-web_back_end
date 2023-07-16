export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  static get [Symbol.species]() {
    return this;
  }

  cloneCar() {
    const Species = this.constructor[Symbol.species];
    const { this: _brand, this: _motor, this: _color } = this;
    const object = new Species(_brand, _motor, _color);
    return object;
  }
}
