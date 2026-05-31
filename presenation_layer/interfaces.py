from abc import ABC, abstractmethod


class IConsoleView(ABC):

    @abstractmethod
    def show_message(self, message):
        pass