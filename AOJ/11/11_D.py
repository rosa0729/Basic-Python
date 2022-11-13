class Dice():

    def __init__(self, table):
        self.number = table

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

    def same(self, another):
        for s in 'NNNNWNNNWNNNENNNENNNWNNN':
            self.direction(s)
            if self.number == another.number:
                return True
        return False


n = int(input())
dice_1 = Dice(list(map(int, input().split())))

Dicelist = []
for i in range(n-1):
    dice_tmp = Dice(list(map(int, input().split())))
    Dicelist.append(dice_tmp)

ans = "Yes"
for o in range(n-1):
    if Dicelist[o].same(dice_1):
        ans = "No"
        break

print(ans)
