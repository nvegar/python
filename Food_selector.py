from secrets import choice


print("Which options for breakfast today?")

food = choice(["apple", "grape", "bacon", "steak", "dirt", "worm"])
food = input()
if food == "apple" or food == "grape":
    print("fruit")
elif food == "bacon" or food == "steak":
    print("meat")
else:
    print("yuck")