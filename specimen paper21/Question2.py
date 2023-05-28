# a
class HiddenBox:
    # __BoxName = String
    # __Creator = String
    # __DateHidden = String
    # __LastFinds = [10][2] String
    # __Active = Boolean
# b
    def __init__(self, Name, Creator, DataHidden, GameLocation):
        self.__Name = Name
        self.__Creator = Creator
        self.__DataHidden = DataHidden
        self.__GameLocation = GameLocation
        self.__Active = False
        self.__LastFinds = [["", ""]for i in range(10)]
# c
    def GetBoxName(self): return self.__Name
    def GetGameLocation(self): return self.__GameLocation


# di
TheBoxes = [HiddenBox("", "", "", "") for i in range(10000)]


# ii
def NewBox():
    global TheBoxes
    name = input("Enter name: ")
    creator = input("Enter creator: ")
    data_hidden = input("Enter the data hidden: ")
    location = input("Enter the game location: ")
    my_box = HiddenBox(name, creator, data_hidden, location)
    TheBoxes.append(my_box)


# iii
NewBox()


# e
class PuzzleBox(NewBox):
    def __init__(self, Name, Creator, DataHidden, GameLocation, PuzzleText, Solution):
        super().__init__(Name, Creator, DataHidden, GameLocation)
        self.__PuzzleText = PuzzleText
        self.__Solution = Solution











