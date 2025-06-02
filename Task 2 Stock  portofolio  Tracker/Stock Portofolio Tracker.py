# Step 1: Hardcoded dictionary of stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 135,
    "AMZN": 120,
    "MSFT": 310
}

# Step 2: Display available stocks
print("=== Stock Portfolio Tracker ===")
print("Available stocks and prices:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

# Step 3: User input for number of stocks
num_stocks = int(input("\nHow many different stocks do you want to enter? "))

portfolio = {}  # To store user stock quantities

# Step 4: Collect user inputs
for i in range(num_stocks):
    stock_name = input(f"\nEnter stock symbol #{i+1} (e.g., AAPL): ").upper()
    if stock_name not in stock_prices:
        print("❌ Stock not found in price list. Try again.")
        continue
    quantity = int(input(f"Enter quantity of {stock_name} shares: "))
    portfolio[stock_name] = quantity

# Step 5: Calculate total investment
total_value = 0
print("\nYour Portfolio:")
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    print(f"{stock} - {qty} shares x ${stock_prices[stock]} = ${value}")
    total_value += value

print(f"\n💰 Total Investment Value: ${total_value}")

# Step 6: Optional — Save to file
save = input("\nDo you want to save the result to a file? (yes/no): ").lower()
if save == 'yes':
    with open("portfolio_summary.txt", "w") as file:
        file.write("Your Portfolio:\n")
        for stock, qty in portfolio.items():
            value = stock_prices[stock] * qty
            file.write(f"{stock} - {qty} shares x ${stock_prices[stock]} = ${value}\n")
        file.write(f"\nTotal Investment Value: ${total_value}\n")
    print("✅ Portfolio saved to 'portfolio_summary.txt'")