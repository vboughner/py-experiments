import sys
import os
import math

def learnLoops():
    print('hello')
    for a in range(1, 3):
        for b in ['y', 'z']:
            print(a, ' ', b)



def myFunction(num):
    mylist = [1, 3, 5, 7, 9, 11, 13]
    mysecondlist = [2, 4, 6, 8, 10, 12]
    combinedlist = mylist + mysecondlist

    if num == 1:
        print(combinedlist)
    elif num == 2:
        for x in range(0, 3):
            print(combinedlist[x])
    elif num == 3:
        tupe = (3, 1, 4)
        print(tupe)
    else:
        print(num)


# myFunction(4)


# let's try a class
class Van:
    def __init__(self, name):
        print("inside constructor")
        self.name = name;

    def show(self):
        print("my name is " + self.name)

    def showMsg(self, msg):
        self.show();
        print(msg)


if __name__ == "__main__":
    learnLoops()
    x = Van("constructor arg")
    x.show();
    x.showMsg("message")

    


