import os
from functions import register, login, validate_ticker, get_historical_closing_prices, save_to_csv, read_from_csv, is_valid_email

def stock_retrieval(email):
    """Stock ticker retrieval and display."""
    print("\nyo bro this is a stock tool")

    while True:
        ticker = input("Enter the Malaysian stock ticker (e.g., 1155.KL for Maybank): ").strip()
        if not validate_ticker(ticker):
            print("Invalid ticker. Please enter a valid Malaysian stock ticker.")
            input("\nPress Enter to try again...")  # Pause before clearing screen
            clear_screen()  # Clear the screen after the invalid ticker input
            continue

        # Get the time period for historical data
        clear_screen()
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
            input("\nPress Enter to try again...")  # Pause before clearing screen
            clear_screen()  # Clear the screen after invalid period choice
            continue

        # Retrieve and display historical data
        clear_screen()
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

    clear_screen()

def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    """Main function that runs the program."""
    is_logged_in = False  # Track the login status of the user
    email = None  # Store the logged-in user's email

    while True:
        clear_screen()
        print("yo bro choose your weapon:")
        print("\nChoose an option:")
        print("1. Register")
        print("2. Login")
        if is_logged_in:
            print("3. View Your Saved Data")
            print("5. Go to Stock Ticker")
        print("4. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            clear_screen()
            register()
        elif choice == "2":
            clear_screen()
            logged_in_email = login()
            if logged_in_email:
                clear_screen()
                print("\nLogin successful!")
                while True:
                    email = input("Enter your email to track your interaction: ").strip()
                    if not is_valid_email(email):
                        print("Invalid email format. Please make sure the email contains '@' and a valid domain.")
                    else:
                        break  # Exit the loop if email is valid
                is_logged_in = True
            else:
                print("\nLogin failed. Please try again.")
        elif choice == "3" and is_logged_in:
            saved_data = read_from_csv(email)  # Pass the logged-in email
            if saved_data is not None:
                print("\nYour Saved Data:")
                print(saved_data.to_string(index=False))
            else:
                print("No saved data found for your account.")
        elif choice == "5" and is_logged_in:
            stock_retrieval(email)  # Go to stock ticker system
        elif choice == "4":
            clear_screen()
            print("beep-boop-beep! BYE-")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

        # Prompt to pause before returning to the menu
        input("\nPress Enter to return to the menu...")

if __name__ == "__main__":
    main()
