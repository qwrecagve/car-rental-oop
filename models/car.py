class Car:
    def __init__(self, car_id, brand, model, price_per_day):
        self.car_id = car_id
        self.brand = brand
        self.model = model
        self.price_per_day = price_per_day
        self.is_available = True

    def rent(self):
        if not self.is_available:
            raise Exception("Mashina allaqachon band!")
        self.is_available = False

    def return_car(self):
        self.is_available = True

    def __str__(self):
        status = "Bo‘sh" if self.is_available else "Band"
        return f"[{self.car_id}] {self.brand} {self.model} - {self.price_per_day}$/kun ({status})"