var assert = require('assert');

const calculateNumber = require("./0-calcul.js");


  describe('sum', () => {
    it(`...`, () => {
      assert.strictEqual(calculateNumber(1, 3), 4);
      });
      it(`...`, () => {
        assert.strictEqual(calculateNumber(1, 3.7), 5);
      });
      it(`...`, () => {
        assert.strictEqual(calculateNumber(1.2, 3.7), 5);
      });
      it(`...`, () => {
        assert.strictEqual(calculateNumber(1.5, 3.7), 6);
      });
  });

  
  
