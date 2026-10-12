
# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 420,
    "GOOGL": 165,
    "AMZN": 190
}

# Store the user's stocks and quantities
portfolio = {}

print("===== STOCK PORTFOLIO TRACKER =====")
print("Available stocks:", ", ".join(stock_prices.keys()))

# Get stock details from the user
while True:
    stock = input("\nEnter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Invalid stock name. Please choose from the available stocks.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

        # Add quantities if the same stock is entered again
        portfolio[stock] = portfolio.get(stock, 0) + quantity

    except ValueError:
        print("Please enter a valid whole number for quantity.")

# Calculate and display the investment value
total_investment = 0

print("\n===== PORTFOLIO SUMMARY =====")

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity
    total_investment += value

    print(
        f"{stock}: {quantity} shares x "
        f"${price} = ${value:,.2f}"
    )

print("------------------------------")
print(f"Total Investment: ${total_investment:,.2f}")

# Optionally save the results
save = input("\nSave results to a text file? (yes/no): ").lower()

if save == "yes":
    with open("stock_portfolio.txt", "w") as file:
        file.write("STOCK PORTFOLIO SUMMARY\n")
        file.write("=======================\n")

        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            value = price * quantity

            file.write(
                f"{stock}: {quantity} shares x "
                f"${price} = ${value:.2f}\n"
            )

        file.write(
            f"\nTotal Investment: ${total_investment:.2f}\n"
        )

    print("Results saved to stock_portfolio.txt")

print("Thank you for using the Stock Portfolio Tracker!")
