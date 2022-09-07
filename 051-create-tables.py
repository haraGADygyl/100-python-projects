from tabulate import tabulate

table = [["Sun", 696000, 1989100000], ["Earth", 6371, 5973.6],
         ["Moon", 1737, 73.5], ["Mars", 3390, 641.85]]

print(tabulate(table))

data = [["Name", "Place", "Gender"], ["Aman", "New Delhi", "Male"], ["Hritika", "New Delhi", "Female"],
        ["Krishna", "UP", "Male"]]

print(tabulate(data))
