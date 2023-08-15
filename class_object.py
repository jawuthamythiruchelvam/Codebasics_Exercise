#q1
class Employee:
   def __init__(self,id,name):
       self.id=id
       self.name=name
   def display(self):
       print(f"name :{self.name} \n ID:{self.id}")

emp = Employee(1, "corder")

#q2
# del the attribute
del emp.id
try :
  print(emp.id)
except AttributeError:
    print("attribute 'ID' not define")

del emp
try:
    emp.display()
except NameError:
    print("emp is not defined")
