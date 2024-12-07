import bcrypt
import pandas as pd
import os

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
