table = [[[0 for i in range(10)]for j in range(3)]for k in range(4)]
n = int(input())
for i in range(n):
    blook, floor, room, add = map(int, input().split())
    table[blook-1][floor-1][room-1] += add
for i in range(4):
    if i != 0:
        print("#"*20)
    for a in range(3):    
        for b in range(10):
            print(" ", table[i][a][b], end='', sep='')
        print()
