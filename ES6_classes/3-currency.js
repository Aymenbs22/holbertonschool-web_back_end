export default class Currency {
  constructor(code, name) {
    this._code = code;
    this._name = name;
  }

  get name() {
    return this._name;
  }

  get code() {
    return this._code;
  }

  set name(Namee) {
    this._name = Namee;
  }

  set code(codee) {
    this._code = codee;
  }

  displayFullCurrency() {
    return `${this.name} (${this.code})`;
  }
}
