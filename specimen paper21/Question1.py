#a
TheData = [20, 3, 4, 8, 12, 99, 4, 26, 4]
#b
def InsertionSort(TheData):
    for count in range(0, len(TheData)):
        DataToInsert = TheData[count]
        Inserted = 0
        NextValue = count - 1
        while NextValue >= 0 and Inserted != 1:
            if DataToInsert < TheData[NextValue]:
                TheData[NextValue + 1] = TheData[NextValue]
                NextValue -= 1
                TheData[NextValue + 1] = DataToInsert
            else:
                Inserted = 1


# c
def outputList(TheData):
    for i in range(len(TheData)):
        print(TheData[i])

# di
print("The unsorted values: ")
outputList(TheData)
print("The sorted values: ")
InsertionSort(TheData)
outputList(TheData)

# ii TESTING

# ei
def search():
    data = int(input("Enter the number to search: "))
    for i in range(len(TheData)):
        if TheData[i] == data:
            print("Found")
            return True
    print('Not found')
    return False
# ii
search()