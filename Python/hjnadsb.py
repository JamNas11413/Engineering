b = "this is something that is just for showing to the user for their better exp"


def mat(lst):
    lst = list(lst)
    for i in lst:
        for j in lst:
            j+=1
            if j % 5 == 0:
                print(i, end="\n")
            else:
                print(i, end=" ")

# mat(b)




print("Hello! World:)")

class DAJE:
    def __init__(self, lst):
        self.lst = lst
    def forl(self):
        for i in lst:
            print(i, end=" ")

d1=DAJE([1,2,3,4,5])
d1.forl()
print("")