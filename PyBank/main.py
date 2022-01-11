# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in profits (date and amount) over the entire period

#import package to allow us to read the file path
import os

#import module for reading cvs file
import csv

#create path that can be run on either Mac or Windows operating system
csv_path=os.path.join('Resources/budget_data.csv')

#initializing variables
month_count = 0
total_revenue = 0
revenue_change = 0
initial_revenue = 0

#creating empty lists for data
revenue = []
monthly_change = []
date = []

with open(csv_path) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first to understand the variables included (optional)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #extracting January
    january_data = next(csvreader)

    month_count_ = month_count + 1 
    total_revenue = total_revenue + int(january_data[1])

    previous_net_profit = int(january_data[1])

#populating the revenue, monthly change, and date lists
    for row in csvreader:
        #count the number of months in a dataset
        month_count = month_count + 1
        #store these results to the date list
        date.append(row[0])
                
        #compute total revenue
        #adding the values for total revenue as an integer
        total_revenue = total_revenue + int(row[1])
        #store the results to the revenue list
        revenue.append(row[1])
        
        #compute monthly change in revenue
        monthly_revenue_change = int(row[1]) - previous_net_profit
        previous_net_profit = int(row[1])        
        #append results to list
        monthly_change.append(monthly_revenue_change)
            
        #computing average change in profits
        avg_revenue_change = round((sum(monthly_change)/len(monthly_change)),2)

        #maximum revenue increase
        greatest_increase = max(monthly_change)

        #date of maximum revenue increase
        max_rev_date = date[monthly_change.index(greatest_increase)]

        #minimum profit increase
        greatest_decrease = min(monthly_change)

        #date of minimum revenue decrease
        min_rev_date = date[monthly_change.index(greatest_decrease)]

#printing the results of the analysis
output = (
f"`````` \n"
f"Financial Analysis \n"
f"-------------------------------- \n"
f"Total Months: {str(month_count)}\n"
f"Total: {str(total_revenue)}\n"
f"Average Change: {str(avg_revenue_change)}\n"
f"Greatest Increase in Profits: {str(max_rev_date)} + {str(greatest_increase)}\n"
f"Greatest Decrease in Profits: {str(min_rev_date)} + {str(greatest_decrease)}\n"
f"``````\n"
)
print(output)
#writing the results of the analysis to a txt file

output_file = os.path.join("Analysis", "financial_output.txt")

with open(output_file, 'w') as file:

    file.write(output)
    