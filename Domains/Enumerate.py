#enumerate for printing ordered list

tasks = ["Buy grocieres", "Clean the room", "Call Mom"]
for index, task in enumerate(tasks, start = 1):
    print(f"{index}.{task}")

#Enumarate for modyfing list by index

prices = [10, 20, 30]
for index, price in enumerate(prices):
    if price > 15:
        prices[index] = price * 0.9

print(prices)

#Enumarate used to track file line Numbers:

with open("teamSorter.py") as file:
    for line_num, line in enumerate(file, start=1):
        if "ERROR" in line:
            print(f"Error found on line {line_num} : {line.strip()}")