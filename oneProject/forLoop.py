noOfCols = int(input("Enter number of columns in the star: "))

for i in range(noOfCols):
    for k in range(i):
        print(" * ", end="")
    print()
