# PyBank

## Background

Tasked with writing a Python program for analyzing the financial records of your company. The data will be provided in a file called budget_data.csv. The dataset is composed of two columns: Date and Profit/Losses.

The program will analyze the the records to calculate each of the following:

  * The total number of months included in the dataset
  
  * The net total amount of Profit/Losses over the entire period
  
  * Calculate the changes in Profit/losses over the entire period, then find the average of those changes
  
  * The greatest increase in profits (date and amount) over the entire period
  
  * The greatest decrease in losses (date and amount) over the entire period
  
  * The analysis should look similar to the this:
  
  
  ```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)
  ```

  * In addition, the program should output the results to the terminal and text file.

## The journey

The simple flow for the program

import necessary modules

create the csv path

open and use the input file

  create the csvreader
  
  read the header line and discard
  
  Initialize several variables used in the loop to process the data
  
  loop through the file one row at a time
  
  increment RowCount by 1, this will also be the number of Months
  
  if RowCount is 1
    gather initial values
      CurrentValue
      TotalValue
      default values for greatest increase and decrease
      
  else
    begin computing data
      PreviousValue = CurrentValue
      CurrentValue = newvalue from file
      compute change in value CurrentValue - PreviousValue
      Append change value to change list
      increment total value by Current value
      determine if there is a change in the greatest increase or decrease
        and capture that data

Upon exiting the loop sum the changes and determine how many values
compute the average change

Print the results to the terminal
print the results to a file

## Problems along the way

The problems alone the way were mostly simple typing errors.  The logic
worked as expected.
