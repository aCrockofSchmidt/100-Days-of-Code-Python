def add(*args):
    sum = 0
    print(args[5])
    for n in args:
        sum += n
    return sum


print(add(1, 2, 3, 4, 5, 6, 7, 8, 9))


def calculate(n, **kwargs):
    for key, value in kwargs.items():
        print(key)
        print(value)

        print(kwargs["add"])

        n += kwargs["add"]
        n *= kwargs["multiply"]
        print(n)

calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw.get("model")
        self.colour = kw.get("colour")

my_car = Car(make="Honda", model="Prelude", colour="Orange")
print(my_car.model)
print(my_car.make)
print(my_car.colour)