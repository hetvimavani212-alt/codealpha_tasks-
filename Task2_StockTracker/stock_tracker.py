stock = {
    "AAPL": 150,
    "MSFT": 300,
    "TCS": 200,
    "TSLA": 700,
    "UBER": 450,
    "ADANI": 900
}

print("\n================================")
print(" Welcome to Stock Tracker ")
print("================================")

print("\n Available Stock List:\n")
for stocks, price in stock.items():
    print(f" {stocks:<10} : {price}")

total_investment = 0
portfolio = []      # Stores all purchased stocks

while True:

    s = input("\n Enter stock name: ").upper()

    if s in stock:

        quantity = int(input(" Enter stock quantity: "))

        investment = stock[s] * quantity

        total_investment += investment

        print(f" Investment in {s}: {investment}")

        portfolio.append({
            "stock": s,
            "quantity": quantity,
            "investment": investment
        })

    else:
        print(f" {s} : Stock not available")

    choice = input("\n Do you want to add another stock? (yes/no): ").lower()

    if choice != "yes":
        break

print("\n ========== Portfolio Summary ==========")

for item in portfolio:
    print(f"{item['stock']}  Quantity: {item['quantity']}  Investment: {item['investment']}")

print(" ---------------------------------------")
print(f" Total Investment = {total_investment}")

with open("portfolio.txt", "w") as file:

    file.write("===== STOCK PORTFOLIO =====\n\n")

    for item in portfolio:
        file.write(
            f"{item['stock']}  - Quantity: {item['quantity']} \n - Investment: {item['investment']}\n"
        )

    file.write("\n -----------------------------\n")
    file.write(f" Total Investment: {total_investment}")

print("\n Portfolio saved to portfolio.txt")
print(" Thank you for using Stock Tracker.")