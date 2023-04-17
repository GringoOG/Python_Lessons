friends = ["Petr", "Honza", "Magda", "Zebra", "Lukáš", "Amálka", "Martin"]
lucky_numbers = [3, 8, 15, 23, 55, 88]

friends.append("Creed")
friends.insert(1, "Mirek")
friends.remove("Petr")
friends.pop()
friends.reverse()
friends.sort()

friends2 = friends.copy()

print(friends)
print(friends2)

cordinates = (4, 5) # tuple, nelze měnit
print(cordinates[0])

cordinates_ = [(4, 5), (15, 23), (55, 68)] # list of tuples