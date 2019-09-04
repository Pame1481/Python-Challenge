import os
import csv

print("Election Results")
print("----------------------------")

# Total number of votes cast  
  
election_csv = os.path.join('election_data.csv')

with open(election_csv,newline ='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csv_header = next(csvfile)
    print(f"Heater: {csv_header}")
    data = list(csvreader)
    row_count = len(data)
    print(f'Total Votes: {row_count}')
    print("----------------------------")

#Candidates, percentages, total number of votes and winner

    total1 = 0
    total2 = 0
    total3 = 0
    total4 = 0

    for row in data:
        if row[2] == "Khan":
            total1 += 1
        if row[2] == "Correy":
            total2 += 1   
        if row[2] == "Li":
            total3 += 1
        if row[2] == "O'Tooley":
            total4 += 1
    print(f'Khan: ({total1}) {(total1/row_count)*100:.3f}%')
    print(f'Correy: ({total2}) {(total2/row_count)*100:.3f}%')
    print(f'Li: ({total3}) {(total3/row_count)*100:.3f}%')
    print(f'O\'Tooley: ({total4}) {(total4/row_count)*100:.3f}%')
    
    Winner = [total1, total2, total3, total4]  
    Winner_name = ("Khan","Correy","Li","O'Tooley")
    print(f'Winner: {Winner_name[Winner.index(max(Winner))]}')

      