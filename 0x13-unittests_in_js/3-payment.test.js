const sendPaymentRequestToApi = require('./3-payment');
const utils = require('./utils');

const expect = require('chai').expect;
const sinon = require('sinon');

describe('endPaymentRequestToApi', () => {
  it('should return sendPaymentRequestToApi(100, 20)', () => {
    const spy = sinon.spy(utils, 'calculateNumber');
    const spyCon = sinon.spy(console, 'log');
    const reqApi = sendPaymentRequestToApi(100, 20);
  
    expect(spy.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
    expect(spyCon.calledWithExactly('The total is: 120')).to.be.true;
    expect(utils.calculateNumber('SUM', 100, 20)).to.equal(reqApi);
  });
});
