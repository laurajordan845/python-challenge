#Challenge 3 - PyPoll - Laura Jordan

#import depedencies
import os
import csv

#read CSV file
with open("./election_data.csv", 'r') as csvfile:

    #split data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #define the variables needed 
    totalvotes = 0
    votespercandidate = {}

    #file headers
    header = next(csvreader)

    #find candidates and count votes
    for row in csvreader:
        totalvotes += 1
        if row[2] not in votespercandidate:
            votespercandidate[row[2]] = 1
        else:
            votespercandidate[row[2]] +=1

#print initial information we have - title, line breaks, and total votes
print("Election Results")
print("---------------------")
print("Total Votes: " + str(totalvotes))
print("---------------------")

#calculate and print percentage of votes per candidate and line break
for candidate, votes in votespercandidate.items():
    print(candidate + ": " "{:.3%}".format(votes/totalvotes)+" ("+str(votes) +")")
    print("---------------------")

#find candidate with most votes and print winner's name and line break
winner = max(votespercandidate, key=votespercandidate.get)
print(f"Winner: {winner}")
print("---------------------")

#write to text file
f = open("pypoll - ljordan.txt", "w")
f.write("Election Results")
f.write("---------------------")
f.write("Total Votes: " + str(totalvotes))
f.write("---------------------")
f.write(candidate + ": " "{:.3%}".format(votes/totalvotes)+" ("+str(votes) +")")
f.write("---------------------")
f.write(f"Winner: {winner}")
f.write("---------------------")



