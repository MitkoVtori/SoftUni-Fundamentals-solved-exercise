coffee = 0
lower_case = ["dog", "cat", "movie", "coding"]
upper_case = ["DOG", "CAT", "MOVIE", "CODING"]
command = str(input())
while command != "END":
    if command in lower_case:
        coffee += 1
    elif command in upper_case:
        coffee += 2

    command = str(input())

if coffee > 5:
    print("You need extra sleep")
else:
    print(coffee)
