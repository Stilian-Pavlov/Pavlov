n = int(input())

for i in range(n):
    lines = input()
    if "," in lines:
        print(f"{lines} is not pure!")
    elif "." in lines:
        print(f"{lines} is not pure!")
    elif "_" in lines:
        print(f"{lines} is not pure!")
    else:
        print(f"{lines} is pure.")
