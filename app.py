## Odd/Even identifiers

""" x = input("Pick a number:")
if int(x) % 2 == 0:
    print("even")
else:
    print("odd")
 """

## Tip Calculator
""" x_initialBill = input("What is your bill total?")
x_tipValue = input("How was the service? Bad , Okay , Good , Great " )
if x_tipValue == "Bad":
    print("0% tip")
    print((int(x_initialBill) * (1 + (0.01 * 0))))
elif x_tipValue == "Okay":
    print("15%")
    print((int(x_initialBill) * (1 + (0.01 * 15))))
elif x_tipValue == "Good":
    print("20%")
    print((int(x_initialBill) * (1 + (0.01 * 20))))
elif x_tipValue == "Great":
    print("25%")
    print(((int(x_initialBill) * (1 + (0.01 * 25)))))
else:
    print("Capitalize or choose another option")
 """

 ## Factor Function

""" x_integer = input("Choose a Number ")
for i in range(int(x_integer)):
    if (i) > 0 and int(x_integer) % (i) == 0:
        print(i) """

## Greatest common factor function



factor1st = []
factor2nd = []

x_1stInteger = input("Choose a Number")
x_2ndInteger = input("Choose Another Number")


for x in range(int(x_1stInteger)):
    if (x) > 0 and (int(x_1stInteger) % x == 0):
        factor1st.append(x)

for y in range(int(x_2ndInteger)):
    if (y) > 0 and (int(x_2ndInteger) % y == 0):
        factor2nd.append(y)

if 