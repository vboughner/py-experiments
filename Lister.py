

# a comment about my class
class Lister:
    def __init__(self):
        print('''
  initializing lister class
    like this
        ''')

    @staticmethod
    def demo():
        print("Demo at %s done in %s %d times\n" % ("foo man", "too", 46))
        my_list = [1, 3, 5, 7, 9, 11, 13]
        print(my_list)
        for x in range(0, 7, 2):
            print("here is a", my_list[x])
    @staticmethod
    def addThings(a1, a2):
        return a1 + a2


Lister().demo()

print(Lister.addThings(1, 2))
print(Lister.addThings("friend or ", "foe"))


