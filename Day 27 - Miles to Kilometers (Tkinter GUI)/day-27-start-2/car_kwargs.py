class Car:

    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw.get("model")
        # if key is not available, get returns None (no error)


my_car = Car(make="Honda", model="Accord")
print(my_car.make)