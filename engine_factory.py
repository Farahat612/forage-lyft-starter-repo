from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

class EngineFactory:
    @staticmethod
    def create_engine(engine_type, last_service_date, **kwargs):
        if engine_type == "Capulet Engine":
            return CapuletEngine(last_service_date, **kwargs)
        elif engine_type == "Willoughby Engine":
            return WilloughbyEngine(last_service_date, **kwargs)
        elif engine_type == "Sternman Engine":
            return SternmanEngine(last_service_date, **kwargs)
        else:
            raise ValueError("Invalid engine type")
