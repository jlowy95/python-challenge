# PyBank Challenge
#
# Create a Python script that analyzes the records
# to calculate each of the following:
# 1. total number of months included in the dataset
# 2. net total amount of "Profit/Losses" over the entire period
# 3. average of the changes in "Profit/Losses" over the entire period
# 4. greatest increase in profits (date and amount) over the entire period
# 5. greatest decrease in losses (date and amount) over the entire period
# Write the results to both the terminal and a text file


# OS Library for compatibility across platforms reading file paths
import os
# CSV Library for use of the .csv data files
import csv


# Set the file path to "budget_data.csv" as "bd_filepath"
bd_filepath = os.path.join("..","PyBank","budget_data.csv")

# Variables
# Initialize month counter to 0
months_count = 0
# Initialize profit/loss total to 0
net_total = 0
# Average will be calculated as: (end value - initial value)/months_count
# These values will be assigned within the csv file work loop
# Greatest increase/decrease in p/l will be recorded by "profit_max" and 
# "loss_max" respectively.  Their accompanying months will be recorded by
# "profit_month" and "loss_month".  These will be initialized to the
# first month's values.
profit_max = 0
loss_max = 0


# Results Function
# Stores each line (string) of the desired results in a list.
# Inputs are 'months_count', 'net_total', 'average', 'max_profit',
# 'max_profit_month', 'min_profit', 'min_profit_month'
def result_list(months_count, net_total, average, max_profit, max_profit_month, min_profit, min_profit_month):
    results = [
        "Financial Analysis",
        "----------------------------",
        'Total Months: ' + str(months_count),
        'Total: $' + str(net_total),
        'Average Change: $' + str(average),
        'Greatest Increase in Profits: ' + max_profit_month + ' ($' + str(max_profit) + ')',
        'Greatest Decrease in Profits: ' + min_profit_month + ' ($' + str(min_profit) + ')'
    ]
    return results


# Open the data file to be read as "budget_data"
with open(bd_filepath, newline="") as budget_data:

    csvreader = csv.reader(budget_data, delimiter=",")

    # Skip header row
    header = next(csvreader)
    #delta_temp = int(next(budget_data)[1])
    #print(str(delta_temp))

    for row in csvreader:
        # Increment months_count each month
        months_count += 1
        # Iteratively sum the net total p/l
        net_total += int(row[1])
        
        # For the first instance, initialize start, loss_month and profit_month by 
        # checking if month_count == 1
        if months_count == 1:
            start = int(row[1])
            profit_month = row[0]
            loss_month = row[0]
            profit_max = 0
            loss_max = 0
            delta_pl = 0

        # Find the p/l for each month and average them
        # Initialize during the 2nd month
        if months_count == 2:
            delta_sum = int(row[1]) - start
            delta_temp = int(row[1])
        
        if months_count != 1:
            delta_sum += int(row[1]) - delta_temp
            delta_pl = int(row[1]) - delta_temp
            # delta_temp set after to store the previous value for summing
            delta_temp = int(row[1])


        # Record the end value by re-writing the same variable
        end = int(row[1])

        # Check for greatest p/l
        if delta_pl > profit_max:
            profit_max = delta_pl
            profit_month = row[0]
        if delta_pl < loss_max:
            loss_max = delta_pl
            loss_month = row[0]
        
    # Calculate the average p/l
    average = round(delta_sum / (months_count - 1),2)


# Print Results by using the result_list function from above
results = result_list(months_count, net_total, average, profit_max, profit_month, loss_max, loss_month)
for i in results:
    print(i)


# Write the results to a text file

# Output path
output_path = os.path.join("..","PyBank","financialanalysis.txt")

with open(output_path, 'w') as analysis:

    # Write results
    for i in results:
        analysis.write(i + '\n')

