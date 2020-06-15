from math import sqrt

num = int(input())
is_prime = True

if num == 1:
    is_prime = False
else:
    for i in range(2, round(sqrt(num)) + 1):
        if num % i == 0:
            is_prime = False
            break

print('This number is prime' if is_prime else 'This number is not prime')
