from data_access_layer.database import Base, engine
from data_access_layer.repository import SqlAlchemyRepository
from data_access_layer.data_generator import DataGenerator

from business_layer.services import DataImportService


def main():

    Base.metadata.create_all(bind=engine)

    repository = SqlAlchemyRepository()
    generator = DataGenerator()

    service = DataImportService(
        repository=repository,
        generator=generator
    )

    service.import_data()

    print("1000 records inserted into database!")


if __name__ == "__main__":
    main()