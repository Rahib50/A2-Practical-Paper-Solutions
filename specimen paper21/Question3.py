#3 :)
# a
QueueData = [None for i in range(20)]
StartPointer = 0
EndPointer = 0


# b
def enqueue(data):
    global EndPointer
    if EndPointer != len(QueueData) - 1:
        QueueData[EndPointer + 1] = data
        EndPointer += 1
        return True
    return False


# c
def ReadFile():
    textfile = input("Enter the name of the text file: ")
    try:
        x = True
        file = open(textfile, "r")
        file_line = file.readline().strip()
        while file_line != "":
            x = enqueue(file_line)
            file_line = file.readline().strip()
        if x:
            return 1
        else:
            return 2
    except IOError:
        return -1


# di
x = ReadFile()
if x == 1:
    print("All elements added to queue")
elif x == 2:
    print("Queue full.")
else:
    print("File not found")

# ii test program


# e
def remove():
    global QueueData
    item1 = QueueData[StartPointer]
    item2 = QueueData[StartPointer + 1]
    if item1 != None and item2 != None:
        return f"{item1} {item2}"


