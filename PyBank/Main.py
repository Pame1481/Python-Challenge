import os
import csv

print("Financial Analysis")
print("----------------------------------------------")

# Total number of months included in the dataset  
  
budget_csv = os.path.join('budget_data.csv')

with open(budget_csv,newline ='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csv_header = next(csvfile)
    print(f"Heater: {csv_header}")
    data = list(csvreader)
    row_count = len(data)
    print(f'Total Months: {row_count}')

# Net total amount of "Profit/ Losses" over the entire period
 
    total = 0
    for row in data:
        total += int(row[1])
    print(f'Total: ${total}')

# Average of changes in "Profit/Losses"  
    total2 = 0
    row_before = int(data[0][1])
    for row in data:
        #print(data[1])
        total2 += int(row[1]) - row_before 
        row_before = int(row[1])
    total2 = total2 / (row_count -1)
    print(f'Average Change: ${total2}')
    print("Average Change: ${0:.2f}".format(total2))

# Greatest Increase in "Profit/Losses" over the entire period
    
    row_3 = data[0][0]
    total3 = 0
    row_before = int(data[0][1])
    for row in data:
        aux = int(row[1]) - row_before 
        if aux > total3:
            total3 = aux
            row_3 = row[0]
        row_before = int(row[1])
    print(f'Greatest Increase in Profits: {row_3} $({total3})')
    
    
# Greatest Decrease in "Profit/Losses" over the entire period

    row_4 = data[0][0]
    total4 = 0
    row_before = int(data[0][1])
    for row in data:
        aux = int(row[1]) - row_before 
        if aux < total4:
            total4 = aux
            row_4 = row[0]
        row_before = int(row[1])
    print(f'Greatest Decrease in Profits: {row_4} $({total4})')
  
              
   

