command = input()
while command != "End":

    if command == "Softuni":
        continue
    else:
        print("".join(([x * 2 for x in command])))

    command = input()
