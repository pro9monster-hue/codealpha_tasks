STOCK_PRICES = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "GOOGL": 140.50,
    "AMZN": 135.25
}

def get_portfolio_data():
    portfolio = {}
    print("Stock Portfolio Tracker")
    print("Available stocks and their prices:")
    for ticker, price in STOCK_PRICES.items():
        print(f"- {ticker}: ${price:.2f}")

    print("\nEnter your stock holdings (type 'done' to finish):")
    
    while True:
        ticker = input("Enter stock ticker (e.g., AAPL) or 'done': ").upper()
        if ticker == 'DONE':
            break

        if ticker not in STOCK_PRICES:
            print(f"Stock ticker '{ticker}' not found. Please try again.")
            continue
            
        while True:
            try:
                quantity = int(input(f"Enter quantity for {ticker}: "))
                if quantity <= 0:
                    print("Quantity must be a positive integer.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a whole number for quantity.")
        
        portfolio[ticker] = quantity
        
    return portfolio

def calculate_investment(portfolio):
    total_investment_value = 0.0
    print("\n--- Portfolio Summary ---")
    
    for ticker, quantity in portfolio.items():
        price = STOCK_PRICES[ticker]
        stock_value = price * quantity
        total_investment_value += stock_value
        print(f"{ticker}: {quantity} shares @ ${price:.2f} each = ${stock_value:.2f}")
        
    print(f"\nTotal Investment Value: ${total_investment_value:.2f}")
    return total_investment_value

def save_to_file(portfolio, total_value):
    filename = "portfolio_summary.txt"
    try:
        with open(filename, 'w') as f:
            f.write("Stock Portfolio Summary\n")
            f.write("-----------------------\n")
            for ticker, quantity in portfolio.items():
                price = STOCK_PRICES[ticker]
                stock_value = price * quantity
                f.write(f"{ticker}: {quantity} shares @ ${price:.2f} each = ${stock_value:.2f}\n")
            f.write(f"\nTotal Investment Value: ${total_value:.2f}\n")
        print(f"\nSummary saved to '{filename}' successfully.")
    except IOError:
        print("\nError: Could not save the summary file.")

if __name__ == "__main__":
    my_portfolio = get_portfolio_data()
    if my_portfolio:
        total_value = calculate_investment(my_portfolio)
        save_to_file(my_portfolio, total_value)
    else:
        print("Portfolio is empty. Exiting.")
