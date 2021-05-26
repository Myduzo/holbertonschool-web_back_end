const sendPaymentRequestToApi = require('./5-payment');

const expect = require('chai').expect;
const sinon = require('sinon');

describe('-- HOOKS --', () => {
  let spyCon;
  beforeEach(() => {
    spyCon = sinon.spy(console, 'log');
  });

  it('should return sendPaymentRequestToAPI(100, 20)', () => {
    sendPaymentRequestToApi(100, 20);

    expect(spyCon.calledWithExactly('The total is: 120')).to.be.true;
    expect(spyCon.calledOnce).to.be.true;
  });

  it('should return sendPaymentRequestToAPI(10, 10)', () => {
    sendPaymentRequestToApi(10, 10);

    expect(spyCon.calledWithExactly('The total is: 20')).to.be.true;
    expect(spyCon.calledOnce).to.be.true;
  });

  afterEach(() => {
    spyCon.restore();
  });
});
