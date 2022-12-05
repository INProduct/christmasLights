from abc import ABC, abstractmethod


class Mode(ABC):

    @abstractmethod
    def tear_up(self):
        pass

    @abstractmethod
    def tear_down(self):
        pass

    @abstractmethod
    def loop(self, millis):
        pass
