while True:
    n = int(input())
    if n == 0:
        break
    else:
        def digitsum(n):
            s = str(n)
            array = list(map(int, s))
            return sum(array)

        print(digitsum(n))
