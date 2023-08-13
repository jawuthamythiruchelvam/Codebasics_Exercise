#q1
def triangular_area(base, height):
      area = (1/2)*base*height
      return area

b = float(input("enter base length:"))
h = float(input("enter height :"))
a = triangular_area(base=b, height=h)

print(f"area of triangular is: {a} ")

#q2
def _area(base, height,shape):
      if shape=="triangular":
            area = (1/2)*base*height
            return area
      elif shape=="rectangle":
            area = base*height
            return area
      else:
            print("it is not triangular or rectangle")


b = float(input("enter base length:"))
h = float(input("enter height :"))
s=input("enter the shape:")
ar = _area(base=b, height=h,shape=s)

print(f"area of triangular is: {ar} ")
#q3
def stars(n):
      for i in range(1, n+1):
            for j in range(1, i+1):
                  print("* ", end="")

            print('\n')

num=int(input("enter the number of stars:"))
stars(num)
