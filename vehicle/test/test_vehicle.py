from vehicle.project.vehicle import Vehicle
import unittest


class TestVehicle(unittest.TestCase):

    def setUp(self) -> None:
        self.car = Vehicle(40.5, 320)

    def test_initialization(self):
        self.assertEqual(self.car.fuel, 40.5)
        self.assertEqual(self.car.horse_power, 320)

    def test_init_default_fuel_consumption(self):
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, 1.25)

    def test_drive_not_enough_fuel(self):
        with self.assertRaises(Exception) as context:
            self.car.drive(50)
        self.assertEqual(str(context.exception), "Not enough fuel")

    def test_drive_enough_fuel(self):
        self.car.drive(20)
        self.assertEqual(self.car.fuel, 15.5)

    def test_refuel_failed(self):
        with self.assertRaises(Exception) as context:
            self.car.refuel(10)
        self.assertEqual(str(context.exception), "Too much fuel")

    def test_refuel_successfully(self):
        self.car.drive(20)
        self.car.refuel(20)
        self.assertEqual(self.car.fuel, 35.5)

    def test_print_information(self):
        self.assertEqual(str(self.car), f"The vehicle has 320 " +
                         "horse power with 40.5 fuel left and 1.25 fuel consumption")


if __name__ == '__main__':
    unittest.main()
