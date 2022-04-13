
import csv
import os
os.getcwd()
cwd = os.getcwd() 
print(cwd)
os.chdir(r"C:\\Users\David\Documents\Data Bootcamp\Module 3\Election_Analysis") 
os.getcwd()
print (cwd)

file_to_load = os.path.join("Resources", "election_results.csv")

file_to_save = os.path.join("analysis", "election_analysis.txt")

total_votes = 0
candidate_options = []
candidate_votes ={}
Winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    
    
    for row in (file_reader):                           #>>>Iterate for each list declared as row in the file 
        total_votes +=1                                 #>>>Sum each list in the file    
        
        
        candidate_name = row[2]                         #>>>Find the values in each list, column 2 and declare it as candidate_name
        
        
        if candidate_name not in candidate_options:     #>>>Search for the missing name in the list
            candidate_options.append(candidate_name)    #>>>Creates the list with the names of the candidates (once)   
            
            candidate_votes[candidate_name] = 0         #>>>Creates de dictionary with the names of the candidates value 0 (once)
        candidate_votes[candidate_name] += 1            #>>>Adds +1 to the value for each key in the dictionary each time a name is found 
    
with open(file_to_save, "w") as txt_file:   
    
    election_results = (
         f"\nElection Results\n"
         f"-------------------------\n"
         f"Total Votes : {total_votes:,}\n"
         f"-------------------------\n")
    print(election_results, end="")
    
    txt_file.write(election_results)
    
       
    for candidate_name in candidate_options:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) *100
        #print(f"{candidate_name}:received {vote_percentage:.1f}% of the vote")
       
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name  
            
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)
        
    for candidate in candidate_votes:
        winning_candidate_summary = (  
            f"------------------------\n"
            f"winner:{winning_candidate}\n"
            f"winning vote count : {winning_count:,}\n"
            f"Winning Percentage : {winning_percentage:.1f}%\n"
            f"------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
    
    