#q1
my_set={1,2,3,4,5,6}
f_set=frozenset(my_set)

#q2
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
print("set 1 :", set1)
print("set 2: ", set2)
dif_s1_s2= set1-set2
print("different between set 1 and set 2 :", dif_s1_s2)
dif_s1_s2_f=set1.difference(set2)
print("different between set 1 and set 2 (using difference) :", dif_s1_s2)
