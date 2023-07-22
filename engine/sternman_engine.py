from abc import ABC
from car import Car

class SternmanEngine(Car, ABC):
    def __init__(self, last_service_date, **kwargs):
        super().__init__(last_service_date)
        self.warning_light_is_on = kwargs.get("warning_light_is_on", False)

    def needs_service(self):
        return self.warning_light_is_on
