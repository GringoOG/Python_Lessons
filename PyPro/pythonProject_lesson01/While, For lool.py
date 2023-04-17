i = 1
while  i  <= 10:
    print(i)
    i += 1 # i = i + 1

print("Done with loop")

friends = ["Jim", "Karen", "Kevin"]
for friend  in friends:
    print(friend)

friends = ["Jim", "Karen", "Kevin"]
for index  in range(len(friends)):
    print(friends[index])

for index in range(5):
    if index == 0:
        print("První kolečko")
    else:
        print("Další kolečka")