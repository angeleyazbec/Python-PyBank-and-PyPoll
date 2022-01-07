#import package to allow us to read the file path
import os

#import module for reading cvs file
import csv
#create path that can be run on either Mac or Windows operating system
csv_path=os.path.join('Resources', 'budget_data.csv')

with open(csv_path) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
   csvreader = csv.reader(csvfile, delimiter=',')

   print(csvreader)

    # Read the header row first (skip this step if there is now header)
    #csv_header = next(csvreader)
   # print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
   # for row in csvreader:
    #print(row)

  # The total number of months included in the dataset


  # develop loop to determine the number of months

  # The net total amount of "Profit/Losses" over the entire period
  #loop through again to determine the total revenue for the time period
    
  # Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

  # The greatest increase in profits (date and amount) over the entire period

  # The greatest decrease in profits (date and amount) over the entire period