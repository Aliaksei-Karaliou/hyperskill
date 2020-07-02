from math import log

a = int(input())
b = int(input())

if b > 0 and b != 1:
    log_ab = log(a, b)
else:
    log_ab = log(a)

print(round(log_ab, 2))
