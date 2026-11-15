# --- Exercise 1 ---
# File is in the relative path and opens from Visual Studio with no errors
# --- Exercise 2 ---
import csv
with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)