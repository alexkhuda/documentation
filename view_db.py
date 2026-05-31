from tabulate import tabulate

from data_access_layer.database import SessionLocal
from data_access_layer.models import User, PaymentCard, IssuerCountry


def show_users(session):

    users = session.query(User).all()

    table = []

    for user in users[:20]:

        table.append([
            user.id,
            user.full_name,
            user.email
        ])

    print("\nUSERS\n")
    print(tabulate(
        table,
        headers=["ID", "FULL NAME", "EMAIL"],
        tablefmt="grid"
    ))


def show_cards(session):

    cards = session.query(PaymentCard).all()

    table = []

    for card in cards[:20]:

        table.append([
            card.id,
            card.card_number,
            card.balance,
            card.user.full_name,
            card.country.country_name
        ])

    print("\nPAYMENT CARDS\n")
    print(tabulate(
        table,
        headers=["ID", "CARD NUMBER", "BALANCE", "USER", "COUNTRY"],
        tablefmt="grid"
    ))


def show_countries(session):

    countries = session.query(IssuerCountry).all()

    table = []

    for country in countries:

        table.append([
            country.id,
            country.country_name,
            country.currency
        ])

    print("\nISSUER COUNTRIES\n")
    print(tabulate(
        table,
        headers=["ID", "COUNTRY", "CURRENCY"],
        tablefmt="grid"
    ))


def main():

    session = SessionLocal()

    show_users(session)
    show_cards(session)
    show_countries(session)

    session.close()


if __name__ == "__main__":
    main()