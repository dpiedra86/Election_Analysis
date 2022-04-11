
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

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    for row in next(file_reader):
        print(row)
        
    