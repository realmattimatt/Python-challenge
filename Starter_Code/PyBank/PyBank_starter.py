# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os
# Uncomment line 8 and 9 as needed. 
# A path error was encountered on my personal device. I needed to use the os.getcwd and 
# os.getcwd methods.
print(os.getcwd())
os.chdir(r"c:/Users/mnmat/OneDrive/Desktop/Python-challenge/Starter_Code/PyBank")

# Files to load and output (update with correct file paths)
#file_to_load = r"Resources\budget_data.csv"
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

if os.path.exists(file_to_load):
    print(f"File found: {file_to_load}")
else:
    print(f"File not found: {file_to_load}")

# Define variables to track the financial data
total_months = 0
total_profit_loss = 0
changes = []
greatest_increase = ("", float('-inf'))
greatest_decrease = ("", float('inf'))


# Add more variables to track other necessary financial data"

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)
    # Just to check funtionality so far. 
    #print(header)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    # print("First row of data:", first_row)

    # Track the total and net change
    previous_profit_loss = int(first_row[1])
    total_profit_loss += previous_profit_loss
    total_months += 1

    # Process each row of data
    for row in reader:
        current_profit_loss = int(row[1])
        total_profit_loss += current_profit_loss
        total_months += 1
        
        

        # Track the net change
        change = current_profit_loss - previous_profit_loss
        changes.append(change)

        # Calculate the greatest increase in profits (month and amount)

        if change > greatest_increase[1]:
            greatest_increase = (row[0], change)  # Store the month and amount
        
        # Calculate the greatest decrease in losses (month and amount)
        if change < greatest_decrease[1]:
            greatest_decrease = (row[0], change)
            
        previous_profit_loss = current_profit_loss


# Calculate the average net change across the months
average_change = sum(changes) / len(changes) if changes else 0


# Generate the output summary
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_profit_loss}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
