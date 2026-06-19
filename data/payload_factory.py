# File: data/payload_factory.py

from faker import Faker

fake = Faker()

class PayloadFactory:

    @staticmethod
    def login():

        return {

            "email":
            "eve.holt@reqres.in",

            "password":
            "cityslicka"
        }

    @staticmethod
    def invalid_login():

        return {

            "email":
            fake.email(),

            "password":
            "wrong_password"
        }

    @staticmethod
    def order():

        return {

            "product":
            fake.word(),

            "qty":
            fake.random_int(
                min=1,
                max=5
            )
        }

    @staticmethod
    def large_order():

        return {

            "product":
            "Laptop",

            "qty":
            999
        }

    @staticmethod
    def payment():

        return {

            "amount":
            fake.random_int(
                min=100,
                max=5000
            ),

            "currency":
            "USD"
        }

    @staticmethod
    def invalid_payment():

        return {

            "amount":
            -100,

            "currency":
            "USD"
        }
