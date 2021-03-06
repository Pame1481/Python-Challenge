# PyPoll Solution:

# Dependencies

import os
import csv

print("----------------------------")
print("Election Results:")
print("----------------------------")

# 1. Total number of votes cast  

    # Files to load and output:

election_csv = os.path.join('election_data.csv')

with open(election_csv,newline ='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csv_header = next(csvfile)
    
    data = list(csvreader)
    row_count = len(data)
    print(f'Total Votes: {row_count}')
    print("----------------------------")

# 2. List of candidates, percentages of votes each candidate won, total number of votes each candidate won  

    list_candidates = []
    votes =[]
    candidate_votes = {}
    for row in data:
        votes.append(row[0])
        candidate_name = row[2]
        
        if candidate_name not in list_candidates:
            list_candidates.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
    
    for candidate in list_candidates:
        print(f'{candidate}: ({candidate_votes[candidate]}) {(candidate_votes[candidate]/row_count)*100:.3f}%')

# 3. The winner of the election
   
    max_votes = max(candidate_votes.values())
    
    for candidate_name in candidate_votes:
        if candidate_votes[candidate_name] == max_votes:
            max_votes = candidate_votes[candidate_name]
            winner = candidate_name

            # Print the winning candidate (to terminal)
            print("----------------------------")
            print(f'Winner: {winner}')
            print("----------------------------")
   

      