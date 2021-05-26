const sendPaymentRequestToApi = require('./3-payment');
const Utils = require('./utils');

const expect = require('chai').expect;
const sinon = require('sinon');

describe('endPaymentRequestToApi', () => {
  it('should return sendPaymentRequestToApi(100, 20)', () => {
    const stubFunc = sinon.stub(Utils, 'calculateNumber').returns(10);
    const spyCon = sinon.spy(console, 'log');
    const reqApi = sendPaymentRequestToApi(100, 20);
    

    expect(stubFunc.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
    expect(spyCon.calledWithExactly('The total is: 10')).to.be.true;
    expect(Utils.calculateNumber('SUM', 100, 20)).to.equal(reqApi);
  });
});
