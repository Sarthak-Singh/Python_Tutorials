class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.spaces = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.spaces[carType - 1] != 0:
            self.spaces[carType - 1] -= 1
            return True
        return False


obj = ParkingSystem(1, 1, 0)
print(obj.addCar(1), obj.addCar(2), obj.addCar(3), obj.addCar(1))
