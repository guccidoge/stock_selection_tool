from functions import register, login, validate_ticker, get_historical_closing_prices, save_to_csv, read_from_csv

def stock_retrieval(email):
    print("\nyo bro this is a stock tool")

    while True:
        ticker = input("Enter the Malaysian stock ticker (e.g., 1155.KL for Maybank): ").strip()
        if not validate_ticker(ticker):
            print("Invalid ticker. Please enter a valid Malaysian stock ticker.")
            continue

           # Get the time period for historical data
        print("Select the time period:")
        print("1. 5 Days")
        print("2. 1 Month")
        print("3. 3 Months")
        print("4. 6 Months")
        print("5. 1 Year")
        print("6. 2 Years")
        print("7. 5 Years")
        print("8. Year to Date (YTD)")
        print("9. Max")

        period_choice = input("Enter your choice (1-9): ").strip()

        period_map = {
            "1": "5d",
            "2": "1mo",
            "3": "3mo",
            "4": "6mo",
            "5": "1y",
            "6": "2y",
            "7": "5y",
            "8": "ytd",
            "9": "max"
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

                # Ask user if they want to save to CSV
                save_choice = input("\nDo you want to save this data? (y/n): ").strip().lower()
                if save_choice == 'y':
                    data = {
                        "Email": email,
                        "Stock Ticker": ticker,
                        "Period": period,
                        "Average Price": avg_price,
                        "Highest Price": highest_price,
                        "Lowest Price": lowest_price,
                        "Percentage Change (%)": percentage_change
                    }
                    save_to_csv(data)
                    print("Data saved successfully!")
        else:
            print("Failed to retrieve data. Please check the ticker or time period.")

        # Continue or exit
        cont = input("\nDo you want to retrieve data for another stock? (y/n): ").strip().lower()
        if cont != 'y':
            break

def main():
    """Main function that runs the program."""
    print("yo bro choose your weapon:")
    while True:
        print("\nChoose an option:")
        print("1. Register")
        print("2. Login")
        print("3. View Saved Data")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            register()
        elif choice == "2":
            if login():
                print("\nLogin successful!")
                email = input("Enter your email to track your interaction: ")
                stock_retrieval(email)
            else:
                print("\nLogin failed. Please try again.")
        elif choice == "3":
            # View saved data
            saved_data = read_from_csv()
            if saved_data is not None:
                print("\nSaved Data:")
                print(saved_data)
            else:
                print("No saved data found.")
        elif choice == "4":
            print("beep-boop-beep! BYE-")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
