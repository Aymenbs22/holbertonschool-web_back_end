var expect = require('chai').expect;
  
const calculateNumber = require("./2-calcul_chai.js");


  describe('sum', () => {
    it(`...`, () => {
      expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
      });
  });


  describe('SUBTRACT', () => {
      it(`...`, () => {
        expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
      });
  });

          
  describe('DIVIDE', () => {
    it(`...`, () => {
        expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
        expect(calculateNumber('DIVIDE', 10.3, 0)).to.equal('Error');
        expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
      });    
  });
