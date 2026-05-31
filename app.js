const express = require("express");
const bodyParser = require("body-parser");
const methodOverride = require("method-override");

const paymentRoutes = require("./routes/paymentRoutes");

const app = express();

app.set("view engine", "ejs");

app.use(express.static("public"));
app.use(bodyParser.urlencoded({ extended: true }));
app.use(methodOverride("_method"));

app.use("/", paymentRoutes);

app.listen(3000, () => {
    console.log("Server started on http://localhost:3000");
});