const Utils = require("./utils.js");

function sendPaymentRequestToApi(totalAmount, totalShipping) {
    const PaymentRequest = Utils.calculateNumber("SUM", totalAmount, totalShipping)
    console.log(`The total is: ${PaymentRequest}`);
    return PaymentRequest;
};

module.exports = sendPaymentRequestToApi;
