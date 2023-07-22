from datetime import datetime
from engine_factory import EngineFactory
from car import Battery

class Glissade:
    def __init__(self, last_service_date, engine_type, battery_type, **kwargs):
        self.engine = EngineFactory.create_engine(engine_type, last_service_date, **kwargs)
        self.battery = Battery(last_service_date)

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()
