var expect = require('chai').expect;
var sinon = require("sinon");
  
const calculateNumber = require("./3-payment.js");


  describe('sum', () => {
    it(`...`, () => {
      expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
      });
  });

  describe('test map', () => {
    const operation = sinon.spy();

    it('calls operation', () => {
        expect(operation.called);
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
