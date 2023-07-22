from abc import ABC, abstractmethod
from datetime import datetime, timedelta

class Car(ABC):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self):
        pass

class Battery:
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    def needs_service(self):
        today = datetime.today().date()
        service_threshold = self.last_service_date + timedelta(days=2*365)
        return service_threshold <= today
