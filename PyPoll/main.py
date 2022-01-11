# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote

# import package to create file paths across operating systems
import os

# import package for reading CSV files
import csv

#defining variables
total_votes= 0

#defining lists
candidates = []
vote_count = []
vote_percent = []

election_data=os.path.join('Resources', 'election_data.csv')

with open(election_data) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
                      
    # read in the header row to understand the variables included
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")  

    for row in csvreader:
        #count the total number of votes
        total_votes += 1
        #adding up the votes for the candidates and appending to dataframe
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            vote_count.append(1)
        else:
            index = candidates.index(row[2])
            vote_count[index] += 1

    #computing the percentage of votes and appending to the list
    for votes in vote_count:
        percentage = round((votes/total_votes)*100,2)
        vote_percent.append(percentage)

    #highest number of votes
    winning_count = max(vote_count)
    index = vote_count.index(winning_count)

    #candidate with the most votes
    winner = candidates[index]

#printing the results
output_file = os.path.join("Analysis", "election_output.txt")

with open(output_file, 'w') as file:
    output = (
    f"`````output \n"
    f"Election Results \n"
    f"------------------------------- \n"
    f"Total Votes: {str(total_votes)} \n"
    f"------------------------------- \n")
    print(output)
    file.write(output)
    #print candidate name, total votes, vote percentage
    for i in range(len(candidates)):
        output2 = (f"{candidates[i]}: {str(vote_percent[i])} ({str(vote_count[i])}) \n")
        print(output2)
        file.write(output2)

    output3 = (
    f"Winner: {str(winner)} \n" )
    print(output3)
    file.write(output3)
    