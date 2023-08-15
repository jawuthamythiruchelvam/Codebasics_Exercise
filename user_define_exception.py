class InvalidAge (Exception):
    def __init__(self, m):
        self.msg = m

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def get_minor_age(self):
        try:
            #age=int(input("enter the age: "))
            if self.age<18 :
                raise InvalidAge("this person age is under 18")

            else:
                print(f"{self.name}s\' age is {self.age}")
                return self.age

        except InvalidAge as e:
            print(e)
p=Person("jana",19)
x=p.get_minor_age()
