W, H, x, y, r = map(int, input() .split())
if r <= x and r <= y and x + r <= W and y + r <= H:
    print('Yes')
else:
    print('No')