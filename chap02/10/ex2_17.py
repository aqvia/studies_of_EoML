import csv

s = 0
with open("sample.csv") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        s += int(row[1])
print(s)
