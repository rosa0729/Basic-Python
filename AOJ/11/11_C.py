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


dice_1 = Dice()
table_1 = list(map(int, input().split()))
dice_1.numberorder(table_1[0], table_1[1], table_1[2], table_1[3], table_1[4], table_1[5])
dice_2 = Dice()
table_2 = list(map(int, input().split()))
dice_2.numberorder(table_2[0], table_2[1], table_2[2], table_2[3], table_2[4], table_2[5])


for s in 'NNNNWNNNWNNNENNNENNNWNNN':
    dice_1.direction(s)
    if dice_1.number == dice_2.number:
        print("Yes")
        break

if dice_1.number != dice_2.number:
    print("No")
