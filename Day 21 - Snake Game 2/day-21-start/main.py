class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")


class Fish(Animal):  # Fish Class inherits attributes / methods of Animal Class
    def __init__(self):
        super().__init__()  # superclass, initialize

    def breathe(self):
        super().breathe()  # same functionality as super class
        print("Doing this underwater.")  # modification (addition) to super method

    def swim(self):
        print("Moving in the water.")


nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)