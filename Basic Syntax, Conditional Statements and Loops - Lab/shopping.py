budget = int(input())
command = input()
while command != "End":
    product = int(command)
    budget -= product
    if budget < 0:
        print(f"You went in overdraft!")
        break
    command = input()
else:
    print("You bought everything needed.")
