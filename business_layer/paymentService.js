const paymentModel = require("../models/paymentModel");

class PaymentService {

    getCards(callback) {

        paymentModel.getAllCards(callback);
    }

    getCard(id, callback) {

        paymentModel.getCardById(id, callback);
    }

    createCard(data, callback) {

        paymentModel.addCard(data, callback);
    }

    editCard(id, data, callback) {

        paymentModel.updateCard(id, data, callback);
    }

    removeCard(id, callback) {

        paymentModel.deleteCard(id, callback);
    }
}

module.exports = new PaymentService();