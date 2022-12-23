#Challenge 3
#find the total number of months included in dataset
#find total amount of Profit/Losses over the entire period
#find the changes in Profit/Losses over entire period
#find the average of those changes
#find the greatest increase in profits (date and amount) over the entire period
#find the greatest decrease in profits (date and amount) over the entire period


#import depedencies
import os
import csv

#read CSV file
with open("./budget_data.csv", 'r') as csvfile:

    #split data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    #for row in csvreader:
    #    print(row)
        #the above code is testing that it is reading file - not part of exercise, can be deleted once done

    #prints file headers - not part of exercise, can be deleted
    header = next(csvreader)
    #print(header)
    
    #define the variables needed for problem
    month_count = []
    profit = []
    profit_change = []

    #find the total number of months included in dataset
    #find total amount of Profit/Losses over the entire period   
    for row in csvreader:
        month_count.append(row[0])
        profit.append(int(row[1]))
    for i in range (len(profit)-1):
            profit_change.append(profit[i+1]-profit[i])


#look at greatest increase and greatest decrease
highestincrease = max(profit_change)
highestdecrease = min(profit_change)

increase_month = profit_change.index(max(profit_change))+1
decrease_month = profit_change.index(min(profit_change))+1

#print everything
#find the total number of months included in dataset
#find total amount of Profit/Losses over the entire period
#find the changes in Profit/Losses over entire period
#find the average of those changes
#find the greatest increase in profits (date and amount) over the entire period
#find the greatest decrease in profits (date and amount) over the entire period

print("Financial Analysis")
print(f"Total Months: {len(month_count)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change: ${round(sum(profit_change)/len(profit_change),2)}")
print(f"Greatest Increase in Profits: {month_count[increase_month]} (${(str(highestincrease))})")
print(f"Greatest Decrease in Profits: {month_count[decrease_month]} (${(str(highestdecrease))})")

#your final script should both print the analysis to the terminal and export a text file with the results.
f = open("pybank-ljordan.txt", "w")
f.write("Financial Analysis")
f.write(f"Total Months: {len(month_count)}")
f.write(f"Total: ${sum(profit)}")
f.write(f"Average Change: ${round(sum(profit_change)/len(profit_change),2)}")
f.write(f"Greatest Increase in Profits: {month_count[increase_month]} (${(str(highestincrease))})")
f.write(f"Greatest Decrease in Profits: {month_count[decrease_month]} (${(str(highestdecrease))})")