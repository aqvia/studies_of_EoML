import csv

data = [[1,"a",1.1],
        [2,"b",1.2],
        [3,"c",1.3]]

with open("output2.csv", "w") as f:
    wr = csv.writer(f)
    for row in data:
        wr.writerow(row)
