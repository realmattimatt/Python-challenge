# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Uncomment line 11 and 12 as needed. 
# A path error was encountered on my personal device. I needed to use the os.getcwd and 
# os.getcwd methods to run directly in VS Code. Works perfect in Bash without lines 11 and 12.
# print(os.getcwd())
# os.chdir(r"c:/Users/mnmat/OneDrive/Desktop/Python-challenge/Starter_Code/PyBank")

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidate_name = []
candidate_vote_total = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_vote_counter = 0

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)
    # print(header) *If needed for clearity in testing.

    # Loop through each row of the dataset and process it
    for name in reader:

        # Print a loading indicator (for large datasets)
        # print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate_name = name[2]

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidate_vote_total:
            candidate_vote_total[candidate_name] = 0

        # Add a vote to the candidate's count
        candidate_vote_total[candidate_name] += 1
        
    

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    print("\nElection Results\n")
    print(f"-------------------------\n")
    print(f"Total Votes: {total_votes}\n")
    print(f"-------------------------\n")
    
    
    

    # Write the total vote count to the text file
    txt_file.write("Election Results\n\n")
    txt_file.write(f"-------------------------\n\n")
    txt_file.write(f"Total Votes: {total_votes}\n\n")
    txt_file.write(f"-------------------------\n\n")

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate, votes in candidate_vote_total.items():
        

        # Get the vote count and calculate the percentage
        vote_percentage = (votes / total_votes) * 100
        print(f"{candidate}: {vote_percentage:.3f}% ({votes})\n")
        txt_file.write(f"{candidate}: {vote_percentage:.3f}% ({votes})\n\n")
    

        # Update the winning candidate if this one has more votes
        if votes > winning_vote_counter:
            winning_vote_counter = votes
            winning_candidate = candidate

        # Print and save each candidate's vote count and percentage
        

    # Generate and print the winning candidate summary
    summary = f"""
-------------------------

Winner: {winning_candidate}

-------------------------
    """
    print(summary)

    # Save the winning candidate summary to the text file
    txt_file.write(summary)