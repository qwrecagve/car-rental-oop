from models.car import Car
from models.customer import Customer
from services.rental_service import RentalService


def menu():
    print("\n===== CAR RENTAL SYSTEM =====")
    print("1. Mashina qo‘shish")
    print("2. Mijoz qo‘shish")
    print("3. Mavjud mashinalar")
    print("4. Ijara olish")
    print("5. Qaytarish")
    print("0. Chiqish")


def main():
    service = RentalService()

    # demo data
    service.add_car(Car(1, "Toyota", "Camry", 50))
    service.add_car(Car(2, "BMW", "X5", 120))

    service.add_customer(Customer(1, "Ali"))

    while True:
        menu()
        choice = input("Tanlang: ")

        try:
            if choice == "1":
                car_id = int(input("ID: "))
                brand = input("Brand: ")
                model = input("Model: ")
                price = float(input("Narx (kun): "))
                service.add_car(Car(car_id, brand, model, price))

            elif choice == "2":
                cid = int(input("Mijoz ID: "))
                name = input("Ism: ")
                service.add_customer(Customer(cid, name))

            elif choice == "3":
                cars = service.list_available_cars()
                for car in cars:
                    print(car)

            elif choice == "4":
                cid = int(input("Mijoz ID: "))
                car_id = int(input("Mashina ID: "))
                service.rent_car(cid, car_id)
                print("Ijara muvaffaqiyatli!")

            elif choice == "5":
                cid = int(input("Mijoz ID: "))
                car_id = int(input("Mashina ID: "))
                service.return_car(cid, car_id)
                print("Qaytarildi!")

            elif choice == "0":
                break

        except Exception as e:
            print("Xatolik:", e)


if __name__ == "__main__":
    main()