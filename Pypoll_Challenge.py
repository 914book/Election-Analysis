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
# Candidate options, candidate votes, candidate counties.
candidate_options = []
candidate_votes = {}
county_votes = {}
# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Winning County and Winning Count Tracker
winning_county = ""
winning_count_county = 0
winning_percentage_county = 0

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
          # Add the county name to the county list.
            candidate_options.append(candidate_county)

           # 2. Begin tracking that county's vote count. 
            county_votes[candidate_county] = 0

        # Add a vote to that county's count.
        county_votes[candidate_county] += 1
    

# Print the candidate vote dictionary.
#print(candidate_options)
#print(total_votes)
#print(candidate_votes)
#print(county_votes)
# Print the final vote count to the terminal.

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

# Determine the percentage of votes for each county by looping through the counts.
# 1. Iterate through the county list.
    for county in county_votes:
        # 2. Retrieve vote count of a county.
        countyvotes = county_votes[county]
        # 3. Calculate the percentage of county votes.
        countyvote_percentage = float(countyvotes) / float(total_votes) * 100
        county_results = (f"{county}: {countyvote_percentage:.1f}% ({countyvotes:,})\n")
        # 4. Print the winning county name and percentages and votes.({votes:,})
        print(county_results)
        # 5. Save the candidate results to our text file.
        txt_file.write(county_results)    

# Determine winning vote count, winning percentage, and candidate.
        if (countyvotes > winning_count_county) and (countyvote_percentage > winning_percentage_county):
            winning_count_county = countyvotes
            winning_county = county
        

# Print the winning candidates' results to the terminal.
    winning_county_summary = (
        f"-------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        f"-------------------------\n")

    print(winning_county_summary)
    # Save the winning county's results to the text file.
    txt_file.write(winning_county_summary)

    # Determine the percentage of votes for each candidate by looping through the counts.
        # 1. Iterate through the candidate list.
    for candidate in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
                f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        # 4. Print the candidate name and percentage of votes.
        print(candidate_results) 
        # 5. Save the candidate results to our text file.
        txt_file.write(candidate_results)

 # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage

    # Print the winning candidates' results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    print(winning_candidate_summary)
    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)

