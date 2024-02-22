from tire.tire import Tire


class CarriganTire(Tire):
    def __init__(self, tire_wear_values):
        self.tire_wear_values = tire_wear_values

        
    def tire_should_be_serviced(self):
        tire_wear = 0
        for value in range(0, len(self.tire_wear_values)):
            if value >= 0.9:
                return True
            tire_wear = tire_wear + self.tire_wear_values[value]

        return tire_wear > 3


    def needs_service(self):
        return self.tire_should_be_serviced()