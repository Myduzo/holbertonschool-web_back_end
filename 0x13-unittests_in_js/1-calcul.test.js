const calculateNumber = require('./1-calcul.js');
const assert = require('assert');

describe('SUM', () => {
  it('checks equality SUM type', () => {
    assert.strictEqual(calculateNumber('SUM',5.3, 2.8), 8);
    assert.strictEqual(calculateNumber('SUM', 7, -6.1), 1);
    assert.strictEqual(calculateNumber('SUM', 0, 3.9), 4);
    assert.strictEqual(calculateNumber('SUM', -2, 0), -2);
    assert.strictEqual(calculateNumber('SUM', -4.1, -8.3), -12);
  });

  it ('TypeError', () => {
    assert.throws(() => calculateNumber('SUM',NaN, 1.8), { name: 'TypeError' });
    assert.throws(() => calculateNumber('SUM',6.4, NaN), { name: 'TypeError' });
    assert.throws(() => calculateNumber('SUM',NaN, NaN), { name: 'TypeError' });
  });
});

describe('SUBTRACT', () => {
  it('checks equality SUBTRACT type', () => {
    assert.strictEqual(calculateNumber('SUBTRACT', 5.3, 2.8), 2);
    assert.strictEqual(calculateNumber('SUBTRACT', 7, -6.1), 13);
    assert.strictEqual(calculateNumber('SUBTRACT', 0, 3.9), -4);
    assert.strictEqual(calculateNumber('SUBTRACT', -2, 0), -2);
    assert.strictEqual(calculateNumber('SUBTRACT', -4.1, -8.3), 4);
  });

  it ('TypeError', () => {
    assert.throws(() => calculateNumber('SUBTRACT', NaN, 3.3), { name: 'TypeError' });
    assert.throws(() => calculateNumber('SUBTRACT', 7.9, NaN), { name: 'TypeError' });
    assert.throws(() => calculateNumber('SUBTRACT', NaN, NaN), { name: 'TypeError' });
  });
});

describe('DIVIDE', () => {
  it('checks equality DIVIDE type', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 8, 2), 4);
    assert.strictEqual(calculateNumber('DIVIDE', 6.1, 2.9), 2);
    assert.strictEqual(calculateNumber('DIVIDE', -2, 1.4), -2);
    assert.strictEqual(calculateNumber('DIVIDE', -4.3, -2.1), 2);
  });

  it ('Error', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 0, 3.3), 'Error');
    assert.strictEqual(calculateNumber('DIVIDE', 7.9, 0), 'Error');
    assert.strictEqual(calculateNumber('DIVIDE', 0, 0), 'Error');
  });

  it ('TypeError', () => {
    assert.throws(() => calculateNumber('DIVIDE', NaN, 3.3), { name: 'TypeError' });
    assert.throws(() => calculateNumber('DIVIDE', 7.9, NaN), { name: 'TypeError' });
    assert.throws(() => calculateNumber('DIVIDE', NaN, NaN), { name: 'TypeError' });
  });
});
