money = int(input())

chicken_cost = 23
goat_cost = 678
pig_cost = 1296
cow_cost = 3848
sheep_cost = 6769

chicken_name = ["chicken", "chickens"]
cow_name = ["cow", "cows"]
pig_name = ["pig", "pigs"]
goat_name = ["goat", "goats"]
sheep_name = ["sheep", "sheep"]

if money >= sheep_cost:
    amount = money // sheep_cost
    index = int(amount > 1)
    print(amount, sheep_name[index])
elif money >= cow_cost:
    amount = money // cow_cost
    index = int(amount > 1)
    print(amount, cow_name[index])
elif money >= pig_cost:
    amount = money // pig_cost
    index = int(amount > 1)
    print(amount, pig_name[index])
elif money >= goat_cost:
    amount = money // goat_cost
    index = int(amount > 1)
    print(amount, goat_name[index])
elif money >= chicken_cost:
    amount = money // chicken_cost
    index = int(amount > 1)
    print(amount, chicken_name[index])
else:
    print("None")
