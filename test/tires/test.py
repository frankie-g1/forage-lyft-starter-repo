from tire.models.Carrigan import CarriganTire 



class TestTires:
    def TestCarriganTires(tire_wear, boolean):
        tires = CarriganTire(tire_wear)
        assert(tires.needs_service() == boolean)
