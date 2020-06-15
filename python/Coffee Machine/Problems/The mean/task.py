count = 0
total_sum = 0
while True:
    num = input()
    if num == '.':
        break
    count += 1
    total_sum += int(num)
print(total_sum / count)
