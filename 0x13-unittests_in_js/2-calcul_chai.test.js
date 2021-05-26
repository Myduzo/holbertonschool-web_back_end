const calculateNumber = require('./2-calcul_chai.js');
const expect = require('chai').expect;

describe('SUM', () => {
  it('checks equality SUM type', () => {
    expect(calculateNumber('SUM', 5.3, 2.8)).to.equal(8);
    expect(calculateNumber('SUM', 7, -6.1)).to.equal(1);
    expect(calculateNumber('SUM', 0, 3.9)).to.equal(4);
    expect(calculateNumber('SUM', -2, 0)).to.equal(-2);
    expect(calculateNumber('SUM', -4.1, -8.3)).to.equal(-12);
  });

  it ('TypeError', () => {
    expect(() => calculateNumber('SUM', NaN, 1.8)).to.throw(TypeError);
    expect(() => calculateNumber('SUM', 6.4, NaN)).to.throw(TypeError);
    expect(() => calculateNumber('SUM', NaN, NaN)).to.throw(TypeError);
  });
});

describe('SUBTRACT', () => {
  it('checks equality SUBTRACT type', () => {
    expect(calculateNumber('SUBTRACT', 5.3, 2.8)).to.equal(2);
    expect(calculateNumber('SUBTRACT', 7, -6.1)).to.equal(13);
    expect(calculateNumber('SUBTRACT', 0, 3.9)).to.equal(-4);
    expect(calculateNumber('SUBTRACT', -2, 0)).to.equal(-2);
    expect(calculateNumber('SUBTRACT', -4.1, -8.3)).to.equal(4);
  });

  it ('TypeError', () => {
    expect(() => calculateNumber('SUBTRACT', NaN, 3.3)).to.throw(TypeError);
    expect(() => calculateNumber('SUBTRACT', 7.9, NaN)).to.throw(TypeError);
    expect(() => calculateNumber('SUBTRACT', NaN, NaN)).to.throw(TypeError);
  });
});

describe('DIVIDE', () => {
  it('checks equality DIVIDE type', () => {
    expect(calculateNumber('DIVIDE', 8, 2)).to.equal(4);
    expect(calculateNumber('DIVIDE', 6.1, 2.9)).to.equal(2);
    expect(calculateNumber('DIVIDE', -2, 1.4)).to.equal(-2);
    expect(calculateNumber('DIVIDE', -4.3, -2.1)).to.equal(2);
  });

  it ('Error', () => {
    expect(calculateNumber('DIVIDE', 0, 3.3)).to.equal('Error');
    expect(calculateNumber('DIVIDE', 7.9, 0)).to.equal('Error');
    expect(calculateNumber('DIVIDE', 0, 0)).to.equal('Error');
  });

  it ('TypeError', () => {
    expect(() => calculateNumber('DIVIDE', NaN, 3.3)).to.throw(TypeError);
    expect(() => calculateNumber('DIVIDE', 7.9, NaN)).to.throw(TypeError);
    expect(() => calculateNumber('DIVIDE', NaN, NaN)).to.throw(TypeError);
  });
});
