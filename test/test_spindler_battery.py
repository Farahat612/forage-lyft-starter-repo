import unittest
from battery.spindler_battery import SpindlerBattery
from datetime import datetime, timedelta

class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = datetime(2023, 1, 1)
        last_service_date = datetime(2021, 1, 1)
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = datetime(2023, 1, 1)
        last_service_date = datetime(2022, 1, 1)
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())

if __name__ == '__main__':
    unittest.main()
