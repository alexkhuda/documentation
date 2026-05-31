from business_layer.interfaces import IDataImporter


class DataImportService(IDataImporter):

    def __init__(self, repository, generator):
        self.repository = repository
        self.generator = generator

    def import_data(self):

        raw_data = self.generator.generate_data(1000)

        cleaned_data = []

        for row in raw_data:

            cleaned_data.append({
                "full_name": row["full_name"],
                "email": row["email"],
                "card_number": row["card_number"],
                "balance": row["balance"],
                "country": row["country"],
                "currency": row["currency"]
            })

        self.repository.save_data(cleaned_data)