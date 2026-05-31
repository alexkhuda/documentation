const sqlite3 = require("sqlite3").verbose();

const db = new sqlite3.Database("./paypal.db");

db.serialize(() => {

    db.run(`
        CREATE TABLE IF NOT EXISTS payment_cards (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            owner_name TEXT,
            email TEXT,
            card_number TEXT,
            balance REAL,
            country TEXT
        )
    `);

});

module.exports = db;