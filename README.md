# Stock Ticker Tool - User Guide

Welcome to the **Stock Ticker Tool**! This tool allows you to retrieve historical stock data for Malaysian stocks and save it for later reference.

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
2. Clone the Repository or Download the ZIP
Clone or download this repository to your local machine:

bash
Copy code
git clone https://github.com/your-username/stock-ticker-tool.git
cd stock-ticker-tool
Or simply download and extract the ZIP file.

3. Use run.bat to Launch the Tool
The tool can be easily launched using a batch file:

Locate and double-click the run.bat file in the project directory.
This will open the terminal window and start the application automatically.
Tool Usage
Step 1: Register or Login
Upon launching the program, you'll be presented with the following options:

1. Register
2. Login
3. View Your Saved Data
4. Exit
5. Go to Stock Ticker Tool
Register: If you are new to the tool, choose option 1 to register an account using your email.
Login: If you already have an account, choose option 2 to log in using your email.
Step 2: Stock Ticker Tool
Once you're logged in, you'll have the option to use the stock selection tool by choosing option 5 (Go to Stock Ticker Tool). Here’s what happens next:

Enter a Stock Ticker: You’ll be prompted to enter a Malaysian stock ticker (e.g., 1155.KL for Maybank). The tool will validate the ticker, so make sure it's correct.

Choose the Time Period: After entering a valid ticker, you’ll need to select the time period for the historical data:

markdown
Copy code
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
The saved data will be stored in a file named saved_data.csv.

Step 3: View Saved Data
To view your saved stock data, go back to the main menu and choose option 3 (View Your Saved Data). The tool will display the stock data you’ve saved, including all historical stock information.

If no data has been saved yet, it will show a message indicating that no records have been found.

Step 4: Exit the Tool
To exit the tool, select option 4 (Exit).

Troubleshooting
Invalid Ticker: If you enter an invalid ticker, the tool will ask you to try again. Make sure to use valid Malaysian stock tickers (e.g., 1155.KL for Maybank).
No Data Found: If the tool says "No records found" for saved data, ensure that you’ve saved data during a stock retrieval session.
Invalid Email: Ensure your email follows the correct format (e.g., example@domain.com) when registering or logging in.
License
This project is licensed under the MIT License - see the LICENSE file for details.

markdown
Copy code

### How to Use This README:
1. **Open VSCode** and create a new file.
2. **Save the file as** `README.md` in your project folder.
3. **Copy and paste** the above content into your `README.md` file.
4. **Preview** your README by clicking on the Markdown preview option in VSCode (press `Ctrl+Shift+V`).

### Upload to GitHub:
To upload the `README.md` file to your GitHub repository, run the following commands in the terminal (inside your project directory):

```bash
git add README.md
git commit -m "Add README with user instructions"
git push origin main
This will upload your README.md file to your GitHub repository, and it will be visible to users who visit your project.
