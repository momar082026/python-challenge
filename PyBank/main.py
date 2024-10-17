# Import necessary libraries
import pandas as pd
import os
 
# Set file paths
input_path = os.path.join(".", "Resources", "budget_data.csv")
output_path = os.path.join(".", "analysis", "budget_analysis.txt")
 
# Read the CSV file
# We use pandas to read the CSV file, which is more efficient for large datasets
df = pd.read_csv(input_path)
 
# Calculate total months
# The number of rows in the dataframe equals the number of months
total_months = len(df)
 
# Calculate total amount
# We sum all values in the 'Profit/Losses' column
total_amount = df['Profit/Losses'].sum()
 
# Calculate changes in profit/losses
# We use the diff() function to calculate the difference between consecutive rows
df['Change'] = df['Profit/Losses'].diff()
 
# Calculate average change
# We exclude the first row (which will be NaN) and calculate the mean
average_change = df['Change'].mean()
 
# Find greatest increase and decrease
# idxmax() and idxmin() return the index of the maximum and minimum values
greatest_increase = df.loc[df['Change'].idxmax()]
greatest_decrease = df.loc[df['Change'].idxmin()]
 
# Prepare the results
results = [
    "Financial Analysis",
    "----------------------------",
    f"Total Months: {total_months}",
    f"Total: ${total_amount:,.0f}",
    f"Average Change: ${average_change:,.2f}",
    f"Greatest Increase in Profits: {greatest_increase['Date']} (${greatest_increase['Change']:,.0f})",
    f"Greatest Decrease in Profits: {greatest_decrease['Date']} (${greatest_decrease['Change']:,.0f})"
]
 
# Print results to console
print('\n'.join(results))
 
# Write results to file
with open(output_path, 'w') as f:
    f.write('\n'.join(results))
 
print(f"\nResults have been saved to {output_path}")
 
# Additional unique analysis: Monthly statistics
print("\nMonthly Statistics:")
print(df['Profit/Losses'].describe())
 
# Visualization of profit/losses over time
import matplotlib.pyplot as plt
 
plt.figure(figsize=(12,6))
plt.plot(df['Date'], df['Profit/Losses'])
plt.title('Profit/Losses Over Time')
plt.xlabel('Date')
plt.ylabel('Profit/Losses')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(".", "analysis", "profit_losses_trend.png"))
plt.close()
 
print("\nA plot of Profit/Losses over time has been saved in the analysis folder.")