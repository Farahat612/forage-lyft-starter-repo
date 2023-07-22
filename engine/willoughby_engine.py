from abc import ABC
from car import Car

class WilloughbyEngine(Car, ABC):
    def __init__(self, last_service_date, **kwargs):
        super().__init__(last_service_date)
        self.current_mileage = kwargs.get("current_mileage", 0)
        self.last_service_mileage = kwargs.get("last_service_mileage", 0)

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 60000
