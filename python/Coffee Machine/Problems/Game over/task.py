scores = input().split()
score = 0
mistakes = 0
succeed = True
for answer in scores:
    if answer == 'C':
        score += 1
    else:
        mistakes += 1

    if mistakes == 3:
        succeed = False
        break

print("You won" if succeed else "Game over")
print(score)
# put your python code here
