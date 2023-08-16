#q1
integer = [0, 1, 2, 3, 4]
binary = ["0", "1", "10", "11", "100"]
#zip is generating these tuples on-the-fly as you iterate, it doesn't need to store
z = zip(integer, binary)
print(type(z))
print(z)
binary_dict={integer:binary for integer,binary in z}
print(binary_dict)

#q2
integer1 = [1, -1, 2, 3, 5, 0, -7]
inverse = [-1*i for i in integer1]
print(inverse)

#q3
integer2 = [1, -1, 2, 3, 5, 0, -7]
sqr={i*i for i in integer2}
print(sqr)
