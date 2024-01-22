"sandbox"

largest = -10000000000000000000
smallest = 10000000000000000000

while 1:
    l = input("type in an integer: ")

    if (l.lstrip("-").isdigit()):
        l = int(l)
        if (l > largest):
            largest = l
        if (l < smallest):
            smallest = l
    else:
        print("largest number: ", largest, "smallest number: ", smallest)
        break