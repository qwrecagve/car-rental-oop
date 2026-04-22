class RentalService:
    def __init__(self):
        self.cars = []
        self.customers = []

    def add_car(self, car):
        self.cars.append(car)

    def add_customer(self, customer):
        self.customers.append(customer)

    def find_car(self, car_id):
        for car in self.cars:
            if car.car_id == car_id:
                return car
        raise Exception("Mashina topilmadi!")

    def find_customer(self, cid):
        for c in self.customers:
            if c.customer_id == cid:
                return c
        raise Exception("Mijoz topilmadi!")

    def rent_car(self, cid, car_id, days):
        car = self.find_car(car_id)
        customer = self.find_customer(cid)
        customer.rent_car(car, days)

    def return_car(self, cid, car_id):
        car = self.find_car(car_id)
        customer = self.find_customer(cid)
        customer.return_car(car)