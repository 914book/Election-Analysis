#Create a list for the counties
#Create a dictionary where the county is the key and the votes cast for each county in the election are the values.
#create an empty string that will hold the county name that had the largest turnout.
#Declare a variable that represents the number of votes that a county received.
#Inside the with open() function - create three if statements to print out voter turnout results
#add the results to output file
#Print the results to the command line.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter and counties.
total_votes = 0
total_counties = 0
# Candidate options, candidate votes, candidate counties.
candidate_options = []
candidate_votes = {}
candidate_county = {}
# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Get the candidate name from each row.
        candidate_name = row[2]
        candidate_county = row[1]
        # If the candidate does not match any existing candidate, add the
        # the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

        if candidate_county not in candidate_options:
          # Add the candidate name to the candidate list.
            candidate_options.append(candidate_county)

           # 2. Begin tracking that candidate's vote count. 
            candidate_votes[candidate_county] = 0

        # Add a vote to that county's count.
        candidate_votes[candidate_county] += 1
    

# Print the candidate vote dictionary.
print(candidate_votes)
# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"\nCounty Votes:\n")
        
        
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
    for candidatecounty in candidate_votes:
        # Retrieve vote count and percentage.
        countyvotes = candidate_votes[candidate_county]
        countyvote_percentage = float(countyvotes) / float(total_votes) * 100
        county_results = (
            f"{candidate_county}: {countyvote_percentage:.1f}% ({countyvotes:,})\n")
        # Print each county's voter count and percentage to the terminal.
        print(county_results)
        #  Save the county results to our text file.
        txt_file.write(county_results)
    for candidate in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)