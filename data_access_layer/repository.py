from data_access_layer.interfaces import IRepository
from data_access_layer.database import SessionLocal

from data_access_layer.models import (
    User,
    PaymentCard,
    IssuerCountry
)


class SqlAlchemyRepository(IRepository):

    def save_data(self, data):

        session = SessionLocal()

        for row in data:

            country = session.query(IssuerCountry).filter_by(
                country_name=row["country"]
            ).first()

            if not country:

                country = IssuerCountry(
                    country_name=row["country"],
                    currency=row["currency"]
                )

                session.add(country)
                session.commit()

            user = User(
                full_name=row["full_name"],
                email=row["email"]
            )

            session.add(user)
            session.commit()

            card = PaymentCard(
                card_number=row["card_number"],
                balance=row["balance"],
                user_id=user.id,
                country_id=country.id
            )

            session.add(card)

        session.commit()
        session.close()