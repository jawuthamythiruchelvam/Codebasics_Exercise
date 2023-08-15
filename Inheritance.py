class Animal:
    def __init__(self,habitat):
        self.habitat=habitat

    def sound(self):
        print("something common")

    def print_habitat(self):
        print(self.habitat)

class dog(Animal):
    def __init__(self,habitat):
        super().__init__(habitat)

    def sound(self):
        print("woof woof")

d=dog("Kennel")
d.print_habitat()
d.sound()
a=Animal("try one")
a.print_habitat()
