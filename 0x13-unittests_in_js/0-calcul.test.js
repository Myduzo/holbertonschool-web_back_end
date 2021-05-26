const calculateNumber = require('./0-calcul.js');
const assert = require('assert');

describe('calculateNumber', () => {
  it('checks equality', () => {
    assert.strictEqual(calculateNumber(3, 5), 8);
    assert.strictEqual(calculateNumber(6.5, 0), 7);
    assert.strictEqual(calculateNumber(0, 6.3), 6);
    assert.strictEqual(calculateNumber(9.2, 3.6), 13);
    assert.strictEqual(calculateNumber(-1.9, -4.1), -6);
    assert.strictEqual(calculateNumber(-1.9, 3.2), 1);
  });
  
  it('TypeError', () => {
    assert.throws(() => calculateNumber(NaN, 1.8), { name: 'TypeError' });
    assert.throws(() => calculateNumber(6.4, NaN), { name: 'TypeError' });
    assert.throws(() => calculateNumber(NaN, NaN), { name: 'TypeError' });
  });
});
