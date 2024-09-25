## Factor calculator

""" x_integer = input("Choose a Number ")
for i in range(int(x_integer)):
    if (i) > 0 and int(x_integer) % (i) == 0:
        print(i) """

## Greatest common factor function

factor1st = []
factor2nd = []
x_Gcommonfac = [] 

x_1stInteger = int(input("Choose a number "))
x_2ndInteger = int(input("choose another number"))


for x in range(int(x_1stInteger)):
    if (x) > 0 and (int(x_1stInteger) % x == 0):
        factor1st.append(x)


for y in range(int(x_2ndInteger)):
    if (y) > 0 and (int(x_2ndInteger) % y == 0):
        factor2nd.append(y)

## Try to identify two similar values in both lists##

for i in range(x_1stInteger):
    if i in range(x_2ndInteger) and (i) > 0:
        if (x_1stInteger % i == 0) and (x_2ndInteger % i == 0):
            x_Gcommonfac.append(i)


print(factor1st)
print(factor2nd)

print(max(x_Gcommonfac))