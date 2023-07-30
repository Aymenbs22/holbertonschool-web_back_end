const Utils = require("./utils.js");

function sendPaymentRequestToApi(totalAmount, totalShipping) {
    const PaymentRequest = Math.round(totalAmount) + Math.round(totalShipping);
    console.log(`The total is: ${PaymentRequest}`);
    return PaymentRequest;
};

module.exports = sendPaymentRequestToApi;
