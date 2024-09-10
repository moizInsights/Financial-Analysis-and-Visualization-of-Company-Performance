import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate

# Load datasets
try:
    income_statement = pd.read_csv('C:/Users/hp/Downloads/income_statement.csv')
    balance_sheet = pd.read_csv('C:/Users/hp/Downloads/balance_sheet.csv')
    cash_flow = pd.read_csv('C:/Users/hp/Downloads/cash_flow.csv')
except FileNotFoundError as e:
    print(f"Error loading data: {e}")
    exit()

# Display full datasets
print("\nIncome Statement:")
print(tabulate(income_statement, headers='keys', tablefmt='psql'))

print("\nBalance Sheet:")
print(tabulate(balance_sheet, headers='keys', tablefmt='psql'))

print("\nCash Flow Statement:")
print(tabulate(cash_flow, headers='keys', tablefmt='psql'))

#explain analysis 

# Calculate Gross Profit Margin
if 'grossProfit' in income_statement.columns and 'totalRevenue' in income_statement.columns:
    income_statement['Gross Profit Margin'] = (income_statement['totalRevenue'] - income_statement['costOfRevenue']) / income_statement['totalRevenue']
    print("\nGross Profit Margin:")
    print(tabulate(income_statement[['date', 'Gross Profit Margin']], headers='keys', tablefmt='psql'))
else:
    print("\nCannot calculate Gross Profit Margin because the required columns are missing in the income statement.")


# Calculate Net Profit Margin
if 'netIncome' in income_statement.columns and 'operatingIncome' in income_statement.columns:
    income_statement['Net Profit Margin'] = income_statement['netIncome'] / income_statement['operatingIncome']
    print("\nNet Profit Margin:")
    print(tabulate(income_statement[['date', 'Net Profit Margin']], headers='keys', tablefmt='psql'))
else:
    print("\nCannot calculate Net Profit Margin because the required columns are missing in the income statement.")

# Calculate Debt to Equity Ratio
if 'totalLiabilities' in balance_sheet.columns and 'shareholdersEquity' in balance_sheet.columns:
    balance_sheet['Debt to Equity Ratio'] = balance_sheet['totalLiabilities'] / balance_sheet['shareholdersEquity']
    print("\nDebt to Equity Ratio:")
    print(tabulate(balance_sheet[['date', 'Debt to Equity Ratio']], headers='keys', tablefmt='psql'))
else:
    print("\nCannot calculate Debt to Equity Ratio because the required columns are missing in the balance sheet.")

# Check and calculate Quick Ratio based on the exact column names in the CSV
if 'Current Assets' in balance_sheet.columns and 'Inventory' in balance_sheet.columns and 'Current Liabilities' in balance_sheet.columns:
    balance_sheet['Quick Ratio'] = (balance_sheet['Current Assets'] - balance_sheet['Inventory']) / balance_sheet['Current Liabilities']
    print("\nQuick Ratio:")
    print(tabulate(balance_sheet[['date', 'Quick Ratio']], headers='keys', tablefmt='psql'))
else:
    print("\nCannot calculate Quick Ratio because the required columns are missing in the balance sheet.")



# Data visualization

# Create a figure to hold all the graphs
plt.figure(figsize=(15, 12))

# Plot 1: Net Income Over Time
if 'date' in income_statement.columns and 'netIncome' in income_statement.columns:
    plt.subplot(3, 1, 1)
    plt.plot(income_statement['date'], income_statement['netIncome'], marker='o', color='green', label='Net Income')
    plt.xlabel('Date')
    plt.ylabel('Net Income')
    plt.title('Net Income Over Time')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()

# Plot 2: Debt to Equity Ratio Over Time
if 'date' in balance_sheet.columns and 'Debt to Equity Ratio' in balance_sheet.columns:
    plt.subplot(3, 1, 2)
    plt.plot(balance_sheet['date'], balance_sheet['Debt to Equity Ratio'], marker='o', color='red', label='Debt to Equity Ratio')
    plt.xlabel('Date')
    plt.ylabel('Debt to Equity Ratio')
    plt.title('Debt to Equity Ratio Over Time')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()

# Adjust layout for better visibility
plt.tight_layout()

# Display the graphs
plt.show()
