import bcrypt
import pandas as pd
import os
import yfinance as yf
import re
from getpass import getpass
from datetime import datetime

# File to store user data
credentials_file = "credentials.csv"

def hash_password(password: str) -> str:
    """Hashes the password using bcrypt."""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def verify_password(stored_hash: str, entered_password: str) -> bool:
    """Verifies the entered password against the stored hash."""
    return bcrypt.checkpw(entered_password.encode(), stored_hash.encode())

def is_valid_email(email: str) -> bool:
    """Validates the email format to ensure it contains '@' and a domain."""
    # Regular expression for basic email validation
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

def register():
    """Registers a new user with email and hashed password."""
    email = input("Enter your email: ")
    
    # Check if the email is valid
    if not is_valid_email(email):
        print("Invalid email format. Please make sure the email contains '@' and a valid domain.")
        return

    password = input("Enter your password: ")
    hashed_password = hash_password(password)
    
    if os.path.exists(credentials_file) and email in pd.read_csv(credentials_file)["Email"].values:
        print("Email already registered.")
        return
    
    pd.DataFrame({"Email": [email], "Password": [hashed_password]}).to_csv(
        credentials_file, mode="a", header=not os.path.exists(credentials_file), index=False
    )
    print("Registration successful!")

def login() -> str:
    """Logs in a user by verifying email and password."""
    email = input("Enter your email: ")

    # Check if the email is valid
    if not is_valid_email(email):
        print("Invalid email format. Please make sure the email contains '@' and a valid domain.")
        return ""  # Return empty string if email is invalid
    
    password = getpass("Enter your password: ")

    if not os.path.exists(credentials_file):
        print("No users registered.")
        return ""  # Return an empty string if no users are registered

    df = pd.read_csv(credentials_file)
    if email in df["Email"].values:
        stored_hash = df.loc[df["Email"] == email, "Password"].values[0]
        if verify_password(stored_hash, password):
            print("Login successful!")
            return email  # Return the email of the logged-in user

    print("Invalid credentials.")
    return ""  # Return an empty string for invalid login

def validate_ticker(ticker: str) -> bool:
    """Validates if the ticker is likely valid."""
    return ticker.endswith(".KL")

def get_historical_closing_prices(ticker: str, period: str):
    """Fetches historical closing prices for a ticker."""
    try:
        return yf.Ticker(ticker).history(period=period)["Close"]
    except Exception:
        print("Error retrieving data.")
        return None

def save_to_csv(data, filename="user_interactions.csv"):
    """Saves data to a CSV file."""
    pd.DataFrame([data]).to_csv(
        filename, mode="a", header=not os.path.exists(filename), index=False
    )

def read_from_csv(email):
    """Reads and filters data from the CSV file based on the provided email."""
    try:
        # Read the CSV file
        data = pd.read_csv("data.csv")
        
        # Filter rows matching the user's email
        filtered_data = data[data['Email'] == email]
        
        if filtered_data.empty:
            return None  # Return None if no data matches the email
        
        return filtered_data
    except FileNotFoundError:
        print("The data file does not exist.")
        return None
    except Exception as e:
        print(f"An error occurred while reading the CSV: {e}")
        return None
