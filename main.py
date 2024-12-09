from functions import register, login, validate_ticker, get_historical_closing_prices

def stock_retrieval():
    print("\nWelcome to the Stock Retrieval System!")

    while True:
        ticker = input("Enter the Malaysian stock ticker (e.g., 1155.KL for Maybank): ").strip()
        if not validate_ticker(ticker):
            print("Invalid ticker. Please enter a valid Malaysian stock ticker.")
            continue

        # Get the time period for historical data
        print("Select the time period:")
        print("1. 1 Week")
        print("2. 1 Month")
        print("3. 6 Months")
        print("4. 1 Year")
        period_choice = input("Enter your choice (1-4): ").strip()

        period_map = {
            "1": "1wk",
            "2": "1mo",
            "3": "6mo",
            "4": "1y"
        }
        period = period_map.get(period_choice)

        if not period:
            print("Invalid choice. Please select a valid option.")
            continue

        # Retrieve and display historical data
        print(f"\nRetrieving data for {ticker} for the last {period}...")
        closing_prices = get_historical_closing_prices(ticker, period)

        if closing_prices is not None:
            if closing_prices.empty:
                print("No historical data available for the selected ticker and time period.")
            else:
                print("\nHistorical Closing Prices:")
                print(closing_prices.to_string())

                # Calculate and display statistics
                avg_price = closing_prices.mean()
                percentage_change = ((closing_prices.iloc[-1] - closing_prices.iloc[0]) / closing_prices.iloc[0]) * 100
                highest_price = closing_prices.max()
                lowest_price = closing_prices.min()

                print("\nStatistics for the selected period:")
                print(f"Average Closing Price: {avg_price:.2f}")
                print(f"Percentage Change (First to Last): {percentage_change:.2f}%")
                print(f"Highest Closing Price: {highest_price:.2f}")
                print(f"Lowest Closing Price: {lowest_price:.2f}")
        else:
            print("Failed to retrieve data. Please check the ticker or time period.")

        # Continue or exit
        cont = input("\nDo you want to retrieve data for another stock? (y/n): ").strip().lower()
        if cont != 'y':
            break

def main():
    """Main function that runs the program."""
    print("Welcome bludd!")
    while True:
        print("\nChoose an option:")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            register()
        elif choice == "2":
            if login():
                print("\nLogin successful!")
                stock_retrieval()
            else:
                print("\nLogin failed. Please try again.")
        elif choice == "3":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
