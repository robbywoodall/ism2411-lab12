# --- Exercise 1 ---
# File is in the relative path and opens from Visual Studio with no errors
# --- Exercise 2 ---
import csv
processed = []
total_revenue = 0
with open("data/sales.csv", "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        print(row)
        product, price_str, qty_str = row
        price = float(price_str)
        qty = int(qty_str)
        total = price * qty
        total_revenue += total
        processed.append({"product": product, "price": price, "qty": qty, "total": total})
        print(f"{product}:  {qty} units x ${price:.2f} = ${total:.2f}")
print(f"\nTotal revenue: ${total_revenue:.2f}")