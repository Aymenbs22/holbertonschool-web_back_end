var assert = require('assert');

const calculateNumber = require("./1-calcul.js");


  describe('sum', () => {
    it(`...`, () => {
      assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
      });
  });


  describe('SUBTRACT', () => {
      it(`...`, () => {
        assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
      });
  });


  describe('DIVIDE', () => {
    it(`...`, () => {
        assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
      });
    it(`...`, () => {
        assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
      });
  });
  
  
