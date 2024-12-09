import bcrypt
import pandas as pd
import os
import yfinance as yf
from datetime import datetime, timedelta
from getpass import getpass

# File to store user data
credentials_file = "credentials.csv"

def hash_password(password: str) -> str:
    """Hashes the user's password using bcrypt."""
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password.decode('utf-8')  # Convert to string for storage

def verify_password(stored_hash: str, entered_password: str) -> bool:
    """Verifies the entered password with the stored hashed password."""
    return bcrypt.checkpw(entered_password.encode('utf-8'), stored_hash.encode('utf-8'))

def register():
    """Prompts the user to register with email and password, then stores in a CSV file."""
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    
    # Hash the password before storing it
    hashed_password = hash_password(password)
    
    # Check if the email already exists in the credentials file
    if os.path.exists(credentials_file):
        df = pd.read_csv(credentials_file)
        if email in df["Email"].values:
            print("Email already registered. Please try again.")
            return
    
    # Save the new user data to CSV
    data = {"Email": [email], "Password": [hashed_password]}
    df = pd.DataFrame(data)
    df.to_csv(credentials_file, index=False, mode="a", header=not os.path.exists(credentials_file))
    print("Registration successful!")

def login():
    email = input("Enter your email: ")
    password = getpass("Enter your password: ")

    if not os.path.exists(credentials_file):
        print("No registered users found. Please register first.")
        return False

    df = pd.read_csv(credentials_file)
    if email in df["Email"].values:
        stored_hash = df.loc[df["Email"] == email, "Password"].values[0]
        if verify_password(stored_hash, password):
            return True

    print("Invalid credentials. Please try again.")
    return False
    
def get_historical_closing_prices(ticker: str, period: str):
    try:
        # Fetch data from yfinance
        stock_data = yf.Ticker(ticker)
        historical_data = stock_data.history(period=period)

        # Return only closing prices
        return historical_data['Close']  # 'Close' is case-sensitive
    except Exception as e:
        print(f"Error retrieving data: {e}")
        return None
    
def validate_ticker (ticker: str) -> bool:
    return ticker.endswith(".KL")

def save_to_csv(data, filename="user_interactions.csv"):
 
    # Convert the data dictionary to a DataFrame
    df = pd.DataFrame([data])
    
    # Check if the file already exists
    file_exists = os.path.isfile(filename)
    
    # Save the data to CSV
    df.to_csv(filename, mode="a", header=not file_exists, index=False)

def read_from_csv(filename="user_interactions.csv"):
 
    if not os.path.exists(filename):
        print(f"No data found in {filename}.")
        return None

    # Read the CSV into a DataFrame
    df = pd.read_csv(filename)
    return df
