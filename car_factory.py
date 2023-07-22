from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

class CarFactory:
    # Existing code ...

    @staticmethod
    def create_tire_criteria(tire_wear_array):
        total_wear = sum(tire_wear_array)
        if total_wear >= 3:
            return "Octoprime"
        elif any(wear >= 0.9 for wear in tire_wear_array):
            return "Carrigan"
        else:
            return None

    @staticmethod
    def create_car_with_tires(engine_type, battery_type, tire_wear_array):
        engine = None
        if engine_type == "Capulet":
            engine = CapuletEngine(0, 0)
        elif engine_type == "Willoughby":
            engine = WilloughbyEngine(0, 0)
        elif engine_type == "Sternman":
            engine = SternmanEngine(False)

        battery = None
        if battery_type == "Spindler":
            battery = SpindlerBattery(None, None)  # Pass appropriate date here
        elif battery_type == "Nubbin":
            battery = NubbinBattery(None, None)    # Pass appropriate date here

        car = Car(engine, battery)
        tire_type = CarFactory.create_tire_criteria(tire_wear_array)
        car.set_tire_type(tire_type)  # New method to set tire type
        return car
