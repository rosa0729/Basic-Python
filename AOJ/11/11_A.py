class Dice():

    def __init__(self):
        self.number = [i for i in range(6)]

    def numberorder(self, n0, n1, n2, n3, n4, n5):
        self.number[0] = n0
        self.number[1] = n1
        self.number[2] = n2
        self.number[3] = n3
        self.number[4] = n4
        self.number[5] = n5

    def direction(self, str):

        if str == 'E':
            self.numberorder(self.number[3], self.number[1], self.number[0], self.number[5], self.number[4], self.number[2])
        elif str == 'N':
            self.numberorder(self.number[1], self.number[5], self.number[2], self.number[3], self.number[0], self.number[4])

        elif str == 'S':
            self.numberorder(self.number[4], self.number[0], self.number[2], self.number[3], self.number[5], self.number[1])

        elif str == 'W':
            self.numberorder(self.number[2], self.number[1], self.number[5], self.number[0], self.number[4], self.number[3])

    def topnumber(self):
        return self.number[0]


dice = Dice()
table = list(map(int, input().split()))
dice.numberorder(table[0], table[1], table[2], table[3], table[4], table[5])
str_array = str(input())
for str in str_array:
    dice.direction(str)

print("%d" % (dice.topnumber()))
