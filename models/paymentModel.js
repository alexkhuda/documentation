const db = require("../database/db");

class PaymentModel {

    getAllCards(callback) {

        db.all(
            "SELECT * FROM payment_cards",
            [],
            (err, rows) => {
                callback(rows);
            }
        );
    }

    getCardById(id, callback) {

        db.get(
            "SELECT * FROM payment_cards WHERE id = ?",
            [id],
            (err, row) => {
                callback(row);
            }
        );
    }

    addCard(data, callback) {

        db.run(
            `
            INSERT INTO payment_cards
            (owner_name, email, card_number, balance, country)
            VALUES (?, ?, ?, ?, ?)
            `,
            [
                data.owner_name,
                data.email,
                data.card_number,
                data.balance,
                data.country
            ],
            callback
        );
    }

    updateCard(id, data, callback) {

        db.run(
            `
            UPDATE payment_cards
            SET owner_name = ?,
                email = ?,
                card_number = ?,
                balance = ?,
                country = ?
            WHERE id = ?
            `,
            [
                data.owner_name,
                data.email,
                data.card_number,
                data.balance,
                data.country,
                id
            ],
            callback
        );
    }

    deleteCard(id, callback) {

        db.run(
            "DELETE FROM payment_cards WHERE id = ?",
            [id],
            callback
        );
    }
}

module.exports = new PaymentModel();