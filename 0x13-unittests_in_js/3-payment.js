const Utils = require('./utils.js');

function sendPaymentRequestToApi(totalAmount, totalShipping) {
	const sumCal = Utils.calculateNumber('SUM', totalAmount, totalShipping);
	console.log(`The total is: ${sumCal}`);
	return sumCal;
}

module.exports = sendPaymentRequestToApi;
