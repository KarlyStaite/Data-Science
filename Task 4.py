v = 2000
y=0

while v >= 1000:
    print("After year " + str(y) + " the value of the motorcycle is £" + "%0.2f" %(v))
    y = y + 1
    v = v - (v/10)