class Car:
    def __init__(self, car_id, brand, model, price_per_day):
        self.car_id = car_id
        self.brand = brand
        self.model = model
        self.price_per_day = price_per_day
        self.is_available = True
        self.rented_by = None
        self.days = 0

    def rent(self, customer, days):
        if not self.is_available:
            raise Exception("Mashina band!")
        self.is_available = False
        self.rented_by = customer.name
        self.days = days

    def return_car(self):
        self.is_available = True
        self.rented_by = None
        self.days = 0

    def __str__(self):
        if self.is_available:
            status = "Bo‘sh"
        else:
            total = self.price_per_day * self.days
            status = f"Band ({self.rented_by}, {self.days} kun, {total}$)"
        return f"[{self.car_id}] {self.brand} {self.model} - {self.price_per_day}$/kun | {status}"