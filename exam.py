class Car:
    def __init__(self, fuel=50, fuel_consumption_rate=0.1):
        self.__fuel = fuel   
        self.mileage = 0  
        self.fuel_consumption_rate = fuel_consumption_rate  

    def travel(self, distance):
        
        max_travelable_distance = self.__fuel / self.fuel_consumption_rate
        if distance <= max_travelable_distance:
            self.mileage += distance
            self.__fuel -= distance * self.fuel_consumption_rate
            print(f"Traveled {distance} km.")
        else:
            self.mileage += max_travelable_distance
            self.__fuel = 0
            print(f"Traveled {max_travelable_distance} km and ran out of fuel.")

    def refuel(self, amount):
        
        self.__fuel += amount
        print(f"Refueled {amount} liters. Current fuel: {self.__fuel} liters.")

    def get_remaining_range(self):
        
        return self.__fuel / self.fuel_consumption_rate

    def get_fuel(self):
      
        return self.__fuel

    def set_fuel(self, amount):
        
        if amount >= 0:
            self.__fuel = amount
        else:
            print("Fuel amount cannot be negative.")


car = Car()
car.travel(100)
print(f"Remaining range: {car.get_remaining_range()} km")
car.refuel(20)
print(f"Remaining range: {car.get_remaining_range()} km")
    