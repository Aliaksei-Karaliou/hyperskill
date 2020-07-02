from math import tan, radians

alpha = int(input())
alpha_radians = radians(alpha)
alpha_cotan = 1 / tan(alpha_radians)
print(round(alpha_cotan, 10))