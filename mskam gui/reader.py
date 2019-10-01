import csv
filename  = "data.csv"
fields = []
rows = []
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields = next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

    # get total number of rows

for field in fields:
    print(field,end=" ")
print()
sum = 0
for row in rows:
    sum = sum + int(row[2])
print(sum)
