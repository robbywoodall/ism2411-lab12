
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
high_value = [r for r in processed if r["total"] > 100]
with open("data/cleaned.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Product", "Price", "Qty", "Total"])
    for r in high_value:
        writer.writerow([r["product"], r["price"], r["qty"], f"{r['total']:.2f}"])

print(f"Wrote {len(high_value)} high-value orders to cleaned.csv")
print(f"Original rows: {len(processed)}")