from models.car import Car
from models.customer import Customer
from services.rental_service import RentalService


def menu():
    print("\n===== CAR RENTAL SYSTEM =====")
    print("1. Mashina qo‘shish")
    print("2. Mijoz qo‘shish")
    print("3. Barcha mashinalar")
    print("4. Ijara olish")
    print("5. Qaytarish")
    print("6. Mijozlar ro‘yxati")
    print("7. Faqat bo‘sh mashinalar")
    print("0. Chiqish")


def main():
    service = RentalService()

    # demo data
    service.add_car(Car(1, "Toyota", "Camry", 50))
    service.add_car(Car(2, "BMW", "X5", 120))
    service.add_car(Car(3, "Chevrolet", "Cobalt", 14))
    service.add_car(Car(4, "Kia", "Sonet", 40))

    service.add_customer(Customer(1, "Ali"))
    service.add_customer(Customer(2, "Vali"))
    service.add_customer(Customer(3, "Bek"))
    service.add_customer(Customer(4, "Sher"))

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
                print("Mashina qo‘shildi!")

            elif choice == "2":
                cid = int(input("Mijoz ID: "))
                name = input("Ism: ")
                service.add_customer(Customer(cid, name))
                print("Mijoz qo‘shildi!")

            elif choice == "3":
                print("\n--- Mashinalar ---")
                for car in service.cars:
                    print(car)

            elif choice == "4":
                cid = int(input("Mijoz ID: "))
                car_id = int(input("Mashina ID: "))
                days = int(input("Necha kunga: "))

                service.rent_car(cid, car_id, days)

                car = service.find_car(car_id)
                customer = service.find_customer(cid)

                total = car.price_per_day * days
                print(f"{customer.name} {car.brand} {car.model} ni {days} kunga oldi. Jami: {total}$")

            elif choice == "5":
                cid = int(input("Mijoz ID: "))
                car_id = int(input("Mashina ID: "))

                service.return_car(cid, car_id)

                car = service.find_car(car_id)
                customer = service.find_customer(cid)

                print(f"{customer.name} {car.brand} {car.model} ni qaytardi!")

            elif choice == "6":
                print("\n--- Mijozlar ---")
                for c in service.customers:
                    print(c)

            elif choice == "7":
                print("\n--- Bo‘sh mashinalar ---")
                for car in service.cars:
                    if car.is_available:
                        print(car)

            elif choice == "0":
                print("Dastur tugadi.")
                break

            else:
                print("Noto‘g‘ri tanlov!")

        except Exception as e:
            print("Xatolik:", e)


if __name__ == "__main__":
    main()