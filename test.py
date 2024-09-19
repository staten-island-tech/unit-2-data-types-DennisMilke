l1 = ['a', 'b', 'c']
l2 = ['b', 'c', 'd']
l3 = ['c', 'd', 'e']

l1_l2_and = set(l1) & set(l2)
print(l1_l2_and)
# {'c', 'b'}

print(type(l1_l2_and))
# <class 'set'>

factor1st_list = []
factor2nd_list = []

for x in range(int(x_1stInteger)):
    if (x) > 0 and (int(x_1stInteger) % x == 0):
        factor1st_list.append(x)