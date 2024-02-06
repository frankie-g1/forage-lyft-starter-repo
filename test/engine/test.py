import unittest
from datetime import datetime

from car import Car
from engine.model.capulet_engine import CapuletEngine
from engine.model.sternman_engine import SternmanEngine
from engine.model.willoughby_engine import WilloughbyEngine


class TestEngine:
    def TestCapuletEngine(current_milage, last_service_mileage, boolean):
        engine = CapuletEngine(current_milage, last_service_mileage)
        
        assert(engine.needs_service() == boolean)




if __name__ == "__main__":
    TestEngine.TestCapuletEngine(50000, 10000, True)