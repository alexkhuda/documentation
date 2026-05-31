const sqlite3 = require("sqlite3").verbose();

const db = new sqlite3.Database("./paypal.db");

db.all(
    "SELECT * FROM payment_cards LIMIT 10",
    [],
    (err, rows) => {

        if (err) {
            throw err;
        }

        console.table(rows);
    }
);