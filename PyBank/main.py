# Import files
import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

# Open file


with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    # Initialize variables to be used inside the loop
    PreviousValue = 0
    CurrentValue = 0
    ChangesInValues = []
    TotalValue = 0
    RowCount = 0
    
    # Read each row of data after the header
    for row in csvreader:

        RowCount += 1
        
        if RowCount == 1:
            # No previous data
            CurrentValue = float(row[1])
            TotalValue += CurrentValue
            GreatestIncreaseInValue = 0
            GreatestDecreaseInValue = 0
            GreatestIncreaseMonth = row[0]
            GreatestDecreaseMonth = row[0]
        else:
            # Now we start capturing changes to data
            PreviousValue = CurrentValue
            CurrentValue = int(row[1])
            ChangeInValue = CurrentValue - PreviousValue
            ChangesInValues.append(ChangeInValue)
            TotalValue += CurrentValue
            if ChangeInValue > GreatestIncreaseInValue:
                GreatestIncreaseInValue = ChangeInValue
                GreatestIncreaseMonth = row[0]
            if ChangeInValue < GreatestDecreaseInValue:
                GreatestDecreaseInValue = ChangeInValue
                GreatestDecreaseMonth = row[0]

SumChange = sum(ChangesInValues)
LenChange = len(ChangesInValues)
AverageChange = round(SumChange/LenChange,2)

# Print results to terminal
print(f"Financial Analysis")
print(f"-------------------------------")
print(f"Total Months: {RowCount}")
print(f"Total: ${TotalValue}")
print(f"Average Change: ${AverageChange}") 
print(f"Greatest Increase in Profits: {GreatestIncreaseMonth} ({GreatestIncreaseInValue})")
print(f"Greatest Decrease in Profits: {GreatestDecreaseMonth} ({GreatestDecreaseInValue})")

# Print results to a file
line1 = "Financial Analysis"
line2 = "-------------------------------"
line3 = "Total Months: " + str(RowCount)
line4 = "Total: $" + str(TotalValue)
line5 = "Average Change: $" + str(AverageChange)
line6 = "Greatest Increase in Profits: " + str(GreatestIncreaseMonth) + " (" + str(GreatestIncreaseInValue)+ ")"
line7 = "Greatest Decrease in Profits: " + str(GreatestDecreaseMonth) + " (" + str(GreatestDecreaseInValue)+ ")"
with open('Analysis/FinancialAnalysis.txt','w') as out:
    out.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))
