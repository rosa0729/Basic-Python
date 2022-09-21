import sys

s = sys.stdin.read()

count = [0 for i in range(26)]

for x in s:
    if 'a' <= x.lower() <= 'z':
        count[ord(x.lower()) - ord('a')] += 1

for n in range(26):
    print(chr(97+n), ":", count[n])
