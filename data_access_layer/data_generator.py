import random

from faker import Faker

fake = Faker()

countries = [
    ("USA", "USD"),
    ("Germany", "EUR"),
    ("Ukraine", "UAH"),
    ("Canada", "CAD"),
    ("Poland", "PLN")
]


class DataGenerator:

    def generate_data(self, count=1000):

        data = []

        for _ in range(count):

            country = random.choice(countries)

            data.append({
                "full_name": fake.name(),
                "email": fake.unique.email(),
                "card_number": fake.credit_card_number(),
                "balance": round(random.uniform(100, 10000), 2),
                "country": country[0],
                "currency": country[1]
            })

        return data