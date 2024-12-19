# Stock Selection Tool - User Guide

Welcome to the **My Stock Selection Tool**! This tool allows you to retrieve historical stock data for Malaysian stocks and save it for later reference.

## Features
- **Register and Login**: Users can create an account and log in to track their interactions with the tool.
- **Retrieve Stock Data**: Retrieve historical stock data for a selected Malaysian stock ticker.
- **Save Data**: Save your retrieved stock data for later viewing.
- **View Saved Data**: View your saved stock data anytime after logging in.

## How to Set Up the Tool

### 1. Install Python and Required Libraries

Ensure Python is installed on your computer. You can download it from the official [Python website](https://www.python.org/downloads/).

Install the required Python libraries by running the following command in your terminal:

```bash
pip install pandas
```

### 2. Clone the Repository or Download the ZIP
Clone or download this repository to your local machine:

```bash
git clone https://github.com/guccidoge/stock-Selection-tool.git
cd stock-selection-tool
```
Or simply download and extract the ZIP file.

### 3. Use run.bat to Launch the Tool
The tool can be easily launched using a batch file:

Locate and double-click the run.bat file in the project directory.
This will open the terminal window and start the application automatically.

## Tool Usage
### Step 1: Register or Login
Upon launching the program, you'll be presented with the following options:

```bash
1. Register
2. Login
3. View Your Saved Data
4. Exit
5. Go to Stock Ticker Tool
```
Register: If you are new to the tool, choose option 1 to register an account using your email.
Login: If you already have an account, choose option 2 to log in using your email.

### Step 2: Stock Ticker Tool
Once you're logged in, you'll have the option to use the stock selection tool by choosing option 5 (Go to Stock Ticker Tool). Here’s what happens next:

Enter a Stock Ticker: You’ll be prompted to enter a Malaysian stock ticker (e.g., 1155.KL for Maybank). The tool will validate the ticker, so make sure it's correct.

Choose the Time Period: After entering a valid ticker, you’ll need to select the time period for the historical data:

```bash
1. 5 Days
2. 1 Month
3. 3 Months
4. 6 Months
5. 1 Year
6. 2 Years
7. 5 Years
8. Year to Date (YTD)
9. Max
Type the number corresponding to the desired time period.
```

View Stock Data: The tool will fetch the historical closing prices for the selected stock ticker over the chosen time period. It will display key statistics such as:

Average Closing Price
Percentage Change (First to Last Price)
Highest Closing Price
Lowest Closing Price
Save Data: You will be prompted to save the data. If you want to save it, type y and the data will be saved to a CSV file on your local machine.

The saved data will include the following information:
Email (for tracking purposes)
Stock Ticker
Time Period
Average Price
Highest Price
Lowest Price
Percentage Change
The saved data will be stored in a file named saved_data.csv

Happy coding! xx eilli
