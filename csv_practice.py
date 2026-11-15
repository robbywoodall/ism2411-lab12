
import csv
from datetime import datetime
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
high_value = [r for r in processed if r["total"] > 100]
with open("data/cleaned.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Product", "Price", "Qty", "Total"])
    for r in high_value:
        writer.writerow([r["product"], r["price"], r["qty"], f"{r['total']:.2f}"])

print(f"Wrote {len(high_value)} high-value orders to cleaned.csv")
print(f"Original rows: {len(processed)}")
dict_total_revenue = 0
with open("data/sales.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        product = row["product"]
        price = float(row["price"])
        qty = int(row["quantity"])
        total = price * qty
        dict_total_revenue += total
        print(f"{product}: {qty} units x ${price:.2f} = ${total:.2f}")
print(f"\nDictReader total revenue: ${dict_total_revenue:.2f}")
# DictReader is much cleaner for files with many columns. It will automatically skip the 
# header row and lets you access columns by name.
# csvReader would be better used in smaller files where you are familiar with
# where everything is.
product_summary = {}
with open("data/sales.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        product = row["product"]
        price = float(row["price"])
        qty = int(row["quantity"])
        revenue = price * qty
        if product in product_summary:
            product_summary[product] += revenue
        else:
            product_summary[product] = revenue
print("\nProduct Revenue Summary:")
for product in sorted(product_summary):
    print(f"{product}: ${product_summary[product]:.2f}")
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open("data/run_log.txt", "a") as f:
    f.write(f"{timestamp} - Total Revenue: ${total_revenue:.2f}\n")
print("Run logged successfully!")