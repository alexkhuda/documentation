from abc import ABC, abstractmethod


class IRepository(ABC):

    @abstractmethod
    def save_data(self, data):
        pass