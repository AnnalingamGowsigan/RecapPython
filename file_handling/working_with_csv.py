# working with csv file

import csv
# #write data into a file
# with open("data.csv","w") as file:
#     writer = csv.writer(file)
#     writer.writerow(["product_id", "quantity", "price"])
#     writer.writerow([1000, 100, 65])
#     writer.writerow([1001, 34, 63])
#     writer.writerow([1002, 9, 23])

# read the file
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    # print(list(reader))

    for row in reader:
        print(row)

