#                          simple calculater (using class and object, inheritance, methode,loop, and swich case)


class Addition:
    num1 = None
    num2 = None

    def setdata(self):
        self.num1 = int(input("enter frist number: "))
        self.num2 = int(input("enter secund number: "))

    def getdata(self):
        print(
            "num 1:", self.num1, "num 2: ", self.num2, "= sum of", self.num1 + self.num2
        )


class Multiplication(Addition):
    def getdata(self):
        print(
            "num 1:", self.num1, "num 2: ", self.num2, "= sum of", self.num1 * self.num2
        )


class Subtraction(Addition):
    def getdata(self):
        print(
            "num 1:", self.num1, "num 2: ", self.num2, "= sum of", self.num1 - self.num2
        )


class Divided(Addition):
    def getdata(self):
        print(
            "num 1:", self.num1, "num 2: ", self.num2, "= sum of", self.num1 / self.num2
        )


while True:
    print("1. addition")
    print("2. subtraction")
    print("3. multiplication")
    print("4. divided")
    print("5. exit")
    choice = int(input("enter your choice: "))

    match choice:
        case 1:
            a = Addition()
            a.setdata()
            a.getdata()

        case 2:
            s = Subtraction()
            s.setdata()
            s.getdata()

        case 3:
            m = Multiplication()
            m.setdata()
            m.getdata()

        case 4:
            d = Divided()
            d.setdata()
            d.getdata()

        case 5:
            print("exit")
            break
