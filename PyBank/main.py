#PyBank Challenge
#
#Create a Python script that analyzes the records
# to calculate each of the following:
# 1. total number of months included in the dataset
# 2. net total amount of "Profit/Losses" over the entire period
# 3. average of the changes in "Profit/Losses" over the entire period
# 4. greatest increase in profits (date and amount) over the entire period
# 5. greatest decrease in losses (date and amount) over the entire period


#OS Library for compatibility across platforms reading file paths
import os
#CSV Library for use of the .csv data files
import csv


#Set the file path to "budget_data.csv" as "bd_filepath"
bd_filepath as os.path.join("budget_data.csv")

#Variables
#Initialize month counter to 0
months_count = 0
#Initialize profit/loss total to 0
net_total = 0
#Average will be calculated as: (end value - initial value)/months_count
#These values will be assigned within the csv file work loop
#Change in p/l will be recorded by "delta_pl"
#Greatest increase/decrease in p/l will be recorded by "great_p" and 
#"great_l" respectively.  Their accompanying months will be recorded by
#"great_p_month" and "great_l_month"


#Open the data file to be read as "budget_data"
with open(bd_filepath, newline="") as budget_data:

    csvreader = csv.reader(budget_data, delimiter=",")

