# Necessary libraries
import os
import csv

# Declare vars
votes_total = int()
highest_votes = int()
candidates_dict = dict()
votes_percent = float()
winner = str()
candidates_text = str()

# Path to the election data
csvpath = os.path.join('Resources', 'election_data.csv')

# Open and begin reading the csv, skiping the header
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    # loop through csv collecting needed information
    for row in csvreader:

        # running total of votes
        votes_total = votes_total +1

        # create a dictionary with candidate names as keys
        # and tally votes per candidate
        if row[2] in candidates_dict.keys():
            candidates_dict[row[2]] = candidates_dict[row[2]]+1
        else:
            candidates_dict.update({row[2]: 1})
        
csvfile.close()

# Loop through candidates
for candidate in candidates_dict:

    # Track who has the highest number of votes
    if candidates_dict[candidate] > highest_votes:
        highest_votes = candidates_dict[candidate]
        winner = candidate

    # Find percent votes and store it in a list alongside the number of votes
    votes_percent = round(candidates_dict[candidate] / votes_total * 100, 3)
    candidates_dict[candidate] = [candidates_dict[candidate], votes_percent]

# Create a string of each candidate's stats with a new line between them
for candidate in candidates_dict:
    candidates_text = candidates_text + f"{candidate}: {candidates_dict[candidate][1]}% ({candidates_dict[candidate][0]})\n"

# Output to terminal and txt file
analysis = ("\n"
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {votes_total}\n"
    "-------------------------\n"
    f"{candidates_text}"
    "-------------------------\n"
    f"Winner: {winner}\n"
    "-------------------------\n"
)

print(analysis)

outputpath = os.path.join("Analysis", "election_results.txt")

with open(outputpath, "w") as textfile:
    textfile.write(analysis)