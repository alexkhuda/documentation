const paymentService = require("../business_layer/paymentService");

class PaymentController {

    dashboard(req, res) {

        paymentService.getCards((cards) => {

            res.render("dashboard", { cards });

        });
    }

    addPage(req, res) {

        res.render("add-card");
    }

    create(req, res) {

        paymentService.createCard(req.body, () => {

            res.redirect("/");

        });
    }

    editPage(req, res) {

        paymentService.getCard(req.params.id, (card) => {

            res.render("edit-card", { card });

        });
    }

    update(req, res) {

        paymentService.editCard(
            req.params.id,
            req.body,
            () => {

                res.redirect("/");

            }
        );
    }

    delete(req, res) {

        paymentService.removeCard(
            req.params.id,
            () => {

                res.redirect("/");

            }
        );
    }
}

module.exports = new PaymentController();