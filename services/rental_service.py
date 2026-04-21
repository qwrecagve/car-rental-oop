from models.car import Car
from models.customer import Customer


class RentalService:
    def __init__(self):
        self.cars = []
        self.customers = []

    def add_car(self, car: Car):
        self.cars.append(car)

    def list_available_cars(self):
        return [car for car in self.cars if car.is_available]

    def find_car_by_id(self, car_id):
        for car in self.cars:
            if car.car_id == car_id:
                return car
        return None

    def add_customer(self, customer: Customer):
        self.customers.append(customer)

    def find_customer_by_id(self, customer_id):
        for c in self.customers:
            if c.customer_id == customer_id:
                return c
        return None

    def rent_car(self, customer_id, car_id):
        customer = self.find_customer_by_id(customer_id)
        car = self.find_car_by_id(car_id)

        if not customer or not car:
            raise Exception("Mijoz yoki mashina topilmadi!")

        customer.rent_car(car)

    def return_car(self, customer_id, car_id):
        customer = self.find_customer_by_id(customer_id)
        car = self.find_car_by_id(car_id)

        if not customer or not car:
            raise Exception("Xatolik!")

        customer.return_car(car)