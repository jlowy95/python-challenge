""" PyPoll

You will be give a set of poll data called election_data.csv. 
The dataset has three columns: Voter ID, County, and Candidate. 
Your task is to create a Python script that analyzes the votes 
and calculates each of the following:
1. The total number of votes cast
2. A complete list of candidates who received votes
3. The percentage of votes each candidate won
4. The total number of votes each candidate won
5. The winner of the election based on popular vote.
"""

# Import OS and CSV for compatability with .csv files
import os
import csv

# Create filepath for election_data.csv
election_data_path = os.path.join("..","PyPoll","election_data.csv")

# Variables

#total_votes: tally of all of the votes counted; initialize to 0
total_votes = 0
# candidates: keeps a list of all candidates
candidates = []
# votes_tally: keeps a list of the total votes for each candidate
#   This will be indexed identically to "candidates" for referencing
votes_tally = []
# winner_i: The index of the candidate who earned the most votes
# winner_temp: the comparison variable for votes, initialize to 0
winner_temp = 0


# Results Function
# Stores each line (string) of the desired results in a list.
# Inputs are 'months_count', 'net_total', 'average', 'max_profit',
# 'max_profit_month', 'min_profit', 'min_profit_month'
def result_list(total_votes,candidates, votes_tally, winner_i):
    results = [
        "Election Results",
        "----------------------------",
        'Total Votes: ' + str(total_votes),
        "----------------------------"
    ]
    for i in range(len(candidates)):
        percent_temp = round(votes_tally[i] / total_votes * 100,3)
        results.append(candidates[i] + ":  " + str(percent_temp) + "%  (" + str(votes_tally[i]) + ")")
    results.append("----------------------------")
    results.append("Winner:" + candidates[winner_i])
    results.append("----------------------------")
    return results


# Open and read election_data.csv

with open(election_data_path, newline='') as election_data:
    # Initialize csvreader
    csvreader = csv.reader(election_data, delimiter=',')

    # Skip header
    header = next(csvreader)

    # Process votes
    for row in csvreader:
        # Increment votes
        total_votes += 1

        # If candidate isn't recorded, add to list
        # Append a 0 value (tallied after) to the votes_tally list
        if row[2] not in candidates:
            candidates.append(row[2])
            votes_tally.append(0)

        # Reference candidate list to tally vote
        for i in range(len(candidates)):
            if candidates[i] == row[2]:
                votes_tally[i] += 1


# Find the winner
for i in range(len(votes_tally)):
    if votes_tally[i] > winner_temp:
        winner_i = i

# Print Results
results = result_list(total_votes, candidates, votes_tally, winner_i)
for i in results:
    print(i)

# Write to a text file

# Output file path
output_filepath = os.path.join("..","PyPoll","electionresults.txt")

with open(output_filepath, "w") as election_results:

    for i in results:
        election_results.write(i + '\n')