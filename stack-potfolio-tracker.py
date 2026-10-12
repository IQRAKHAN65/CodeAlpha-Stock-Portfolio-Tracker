# Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}

total_investment = 0
portfolio= []

print("===== STOCK PORTFOLIO TRACKER =====")

while True:
    stock_name = input("\nEnter stock name (or 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))

        if quantity > 0:
            price = stock_prices[stock_name]
            investment = price * quantity
            total_investment += investment
            portfolio.append((stock_name,quantity,price,investment))

            print(f"{stock_name}: {quantity} shares x ${price} = ${investment}")
        else:
            print("Quantity must be greater than zero.")

    else:
        print("Stock not found! Please try again.")

print("\n===== PORTFOLIO SUMMARY =====")

for stock, quantity, price, investment in portfolio:
    print(f"{stock}: {quantity} shares x ${price} = ${investment}")

print(f"\nTotal Investment: ${total_investment}")

with open("portfolio.txt", "w") as file:
    file.write("===== STOCK PORTFOLIO SUMMARY =====\n\n")

    for stock, quantity, price, investment in portfolio:
        file.write(f"Stock: {stock}\n")
        file.write(f"Quantity: {quantity}\n")
        file.write(f"Price per share: ${price}\n")
        file.write(f"Investment: ${investment}\n\n")

    file.write(f"Total Investment: ${total_investment}\n")

print("\nPortfolio saved successfully to portfolio.txt!")
print("Thank you for using Stock Portfolio Tracker!")