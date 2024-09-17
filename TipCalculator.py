
x_initialBill = input("What is your bill total?")
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