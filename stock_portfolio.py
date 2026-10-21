# Stock Portfolio Tracker

portfolio = []

def add_stock():
    name = input("Enter stock name: ")
    quantity = int(input("Enter number of shares: "))
    price = float(input("Enter purchase price per share: "))

    stock = {
        "name": name,
        "quantity": quantity,
        "price": price
    }

    portfolio.append(stock)
    print("Stock added successfully!")

def view_portfolio():
    if not portfolio:
        print("Your portfolio is empty.")
        return

    total_investment = 0

    print("\n--- Your Stock Portfolio ---")

    for stock in portfolio:
        investment = stock["quantity"] * stock["price"]
        total_investment += investment

        print(
            f"Stock: {stock['name']} | "
            f"Shares: {stock['quantity']} | "
            f"Price: Rs.{stock['price']:.2f} | "
            f"Investment: Rs.{investment:.2f}"
        )

    print(f"\nTotal Investment: Rs.{total_investment:.2f}")

while True:
    print("\n===== Stock Portfolio Tracker =====")
    print("1. Add Stock")
    print("2. View Portfolio")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_stock()
    elif choice == "2":
        view_portfolio()
    elif choice == "3":
        print("Thank you for using Stock Portfolio Tracker!")
        break
    else:
        print("Invalid choice. Please try again.")
