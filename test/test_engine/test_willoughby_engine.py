import unittest

from engine.willoughbyEngine import WilloughbyEngine


class TestWilloughbyEngine(unittest.TestCase):
    def test_needs_service_true(self):
        current_mileage = 80001
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        current_mileage = 50000
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())
