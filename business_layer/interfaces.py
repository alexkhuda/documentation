from abc import ABC, abstractmethod


class IDataImporter(ABC):

    @abstractmethod
    def import_data(self):
        pass