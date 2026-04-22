class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name
        self.rented_cars = []

    def rent_car(self, car, days):
        car.rent(self, days)
        self.rented_cars.append(car)

    def return_car(self, car):
        if car not in self.rented_cars:
            raise Exception("Bu mashina sizda yo‘q!")
        car.return_car()
        self.rented_cars.remove(car)

    def __str__(self):
        return f"{self.customer_id} - {self.name}"