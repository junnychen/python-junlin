import os 
import csv
from collections import Counter 


#set file path
csvpath = os.path.join("Resources","election_data.csv")
file_to_output = os.path.join("pypoll_analysis", "Output.txt")

#set all initial value to 0 
total_votes = 0 
candidate1_count = 0 

# create empty lists to store the value while iterating through rows 
total_votes_list = []
candidate_list = []

# open csv, 
with open (csvpath) as electiondata:
    csvreader = csv.reader(electiondata)

    header = next(csvreader)

    for row in csvreader: 
        total_votes_list.append(row[1])
        total_votes = len(total_votes_list)
        candidate_list.append(row[2])
        

    # print(Counter(candidate_list))
    # print(list(Counter(candidate_list).keys())) # equals to list(set(words))
    # print(list(Counter(candidate_list).values())) # counts the elements' frequency

    candidates = list(Counter(candidate_list).keys())
    votes = list(Counter(candidate_list).values())
    # print(candidates)
    # print(votes)
    candidates_votes = list(zip(candidates,votes))
    winner_vote = max(votes)
    # print(winner_vote)
    
    output = ""
    
    # print(f"Election Results")
    output += f"Election Results\n"
    # print(f"-------------------------")
    output += "----------------------\n"
    # print(f"Total vote :({total_votes})")myfile.txt
    output += f"Total vote :{total_votes}\n"
    output += f"-------------------------\n"
    for candidate, vote in candidates_votes:
        
        output += f"{candidate},{'{0:.3f}%'.format(vote/total_votes*100)},{vote}\n"
    output += f"-------------------------\n"
    # print(candidates_votes)
    for candidate, vote in candidates_votes:
        if vote == winner_vote:
            output += f"Winner: {candidate}\n"
    
    print(output)
    
# Election Results
# ----------------------
# Total vote :3521001
# -------------------------
# Khan,63.000%,2218231
# Correy,20.000%,704200
# Li,14.000%,492940
# O'Tooley,3.000%,105630
# -------------------------
# Winner: Khan


# with open("Output.txt", "w") as text_file:
#     text_file.write



    