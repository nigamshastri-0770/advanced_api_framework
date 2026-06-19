# File: data/order_factory.py

from faker import Faker

fake = Faker()

class OrderFactory:

    @staticmethod
    def booking():

        return {
            "firstname": fake.first_name(),
            "lastname": fake.last_name(),
            "totalprice": fake.random_int(min=100, max=500),
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2026-06-18",
                "checkout": "2026-06-20"
            }
        }

    @staticmethod
    def update():

        return {
            "firstname": "Updated",
            "lastname": "User"
        }
