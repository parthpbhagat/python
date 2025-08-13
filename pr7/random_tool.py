import random
import string

class RandomDataGenerator:
    def random_number(self):
        print("*" * 40)
        print("Random number is:", random.randint(1, 100))
        print("*" * 40)

    def random_list(self):
        print("*" * 40)
        print("Random number list:", [random.randint(1, 100) for _ in range(10)])
        print("*" * 40)

        
#  create a random password
    def create_random_password(self):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(characters) for _ in range(6))
        print("*" * 50)
        print("Random Password is:", password)
        print("*" * 50)

    def generate_random_otp(self):
        otp = "".join(random.choice("0123456789") for _ in range(6))
        print("*" * 40)
        print("Generated OTP: ", otp)
        print("*" * 40)
