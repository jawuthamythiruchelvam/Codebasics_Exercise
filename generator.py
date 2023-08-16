import math
def squar_num():
    n=1
    while True:
        yield (pow(n,2))
        n=n+1

values=squar_num()
for i in values:
     if i<100 :
         print(i)
     else:
         break
