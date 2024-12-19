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

def register():
    """Registers a new user with email and hashed password."""
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    while True:
        email = input("Enter your email: ").strip()
        if not re.match(email_pattern, email):
            print("Invalid email format. Please enter a valid email address.")
            continue
        
        if os.path.exists(credentials_file):
            existing_emails = pd.read_csv(credentials_file)["Email"].values
            if email in existing_emails:
                print("Email already registered.")
                return
        
        break

    password = input("Enter your password: ")
    hashed_password = hash_password(password)

    pd.DataFrame({"Email": [email], "Password": [hashed_password]}).to_csv(
        credentials_file, mode="a", header=not os.path.exists(credentials_file), index=False
    )
    print("Registration successful!")

def login() -> str:
    """Logs in a user by verifying email and password."""
    email = input("Enter your email: ")
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

def read_from_csv(email=None):
    """Reads saved data from the CSV file and filters by email."""
    file_path = "user_interactions.csv"
    if not os.path.exists(file_path):
        return None

    try:
        # Load the CSV file
        data = pd.read_csv(file_path)

        # Debug: Print loaded data
        print("Loaded Data from CSV:")
        print(data)

        # Filter data by email
        if email:
            email = email.strip().lower()  # Normalize the input email
            data['Email'] = data['Email'].str.strip().str.lower()  # Normalize the CSV email column
            filtered_data = data[data['Email'] == email]

            # Debug: Print filtered data
            print(f"Filtered Data for Email '{email}':")
            print(filtered_data)

            if filtered_data.empty:
                return None
            return filtered_data
        return data
    except Exception as e:
        print(f"Error reading from CSV: {e}")
        return None
