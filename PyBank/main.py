# Necessary libraries
import os
import csv
import numpy

# Declare vars
months_list = []
profits_list = []
change_list = []
previous_profit = int(0)
months = int(0)
total = int(0)
average = float(0)

# Path to the csv file
csvpath = os.path.join('Resources', 'budget_data.csv')

# Open and begin reading the csv, skiping the header
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    # Create actionable lists from the data in the csv file
    for row in csvreader:
        months_list.append(row[0])
        profits_list.append(int(row[1]))

csvfile.close()

# The total number of months included in the dataset
months = len(months_list)

# The net total amount of "Profit/Losses" over the entire period
total = sum(profits_list)

# The changes in "Profit/Losses" over the entire period, and then the average of those changes
change_list = numpy.diff(profits_list).tolist()
average = round(sum(change_list) / (len(change_list)), 2)

# The greatest increase in profits (date and amount) over the entire period
max_profit = max(change_list)
max_date = months_list[change_list.index(max_profit)+1]

# The greatest decrease in profits (date and amount) over the entire period
min_profit = min(change_list)
min_date = months_list[change_list.index(min_profit)+1]

# Print the analysis to the terminal and export a text file with the results
analysis = (
    "\n"
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {months}\n"
    f"Total: ${total}\n"
    f"Average Change: ${average}\n"
    f"Greatest Increase in Profits: {max_date} (${max_profit})\n"
    f"Greatest Decrease in Profits: {min_date} (${min_profit})"
    "\n"
)

print(analysis)

outputpath = os.path.join("Analysis", "financial_analysis.txt")

with open(outputpath, "w") as textfile:
    textfile.write(analysis)