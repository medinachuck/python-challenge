import os 
import csv 

#import the csv data 
filepath = os.path.join('Resources', 'election_data.csv')
#print(filepath)

with open(filepath) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)

    #Turn iterable into a list 
    poll_data = list(csvreader)

# print(len(poll_data[777][0]))



#ANALYSIS
print('Election Results ')
print('__________________________')
# * The total number of votes cast
    #  total number of votes = number of rows minus 1 for the header
total_votes = (len(poll_data) -1)
print(f'Total Votes: {total_votes}')
print('__________________________')

# * A complete list of candidates who received votes
cleaned_poll_data = list(zip(*poll_data))
#print(cleaned_poll_data[2][0:6])
candidates_df = list(set(cleaned_poll_data[2][1:total_votes]))
candidate_1 = candidates_df[0]
candidate_2 = candidates_df[1]
candidate_3 = candidates_df[2]
candidate_4 = candidates_df[3]

votes_1 = cleaned_poll_data[2].count(candidate_1)
votes_2 = cleaned_poll_data[2].count(candidate_2)
votes_3 = cleaned_poll_data[2].count(candidate_3)
votes_4 = cleaned_poll_data[2].count(candidate_4)

#calculate percentage for each candidate 
p1 = round((votes_1/total_votes) * 100, 3) 
p2 = round((votes_2/total_votes) * 100, 3) 
p3 = round((votes_3/total_votes) * 100, 3)
p4 = round((votes_4/total_votes) * 100, 3) 

print(f'{candidate_1}: {p1}% ({votes_1})\n{candidate_2}: {p2}% ({votes_2})\n{candidate_3}: {p3}% ({votes_3})\n{candidate_4}: {p4}% ({votes_4})')
print('__________________________')
#find winner based on popular vote (max number of votes)
# take votes store them in list.. take max.. match it with candidate
# #non pythonic way of creating list to store variables :( 
candidates_list = [[candidate_1, votes_1], [candidate_2, votes_2],[candidate_3, votes_3], [candidate_4, votes_4]]
grouped_list = list(zip(*candidates_list))
winner_votes = max(grouped_list[1])
winner= str()
for i in range(4): 
    if grouped_list[1][i-1] == winner_votes : 
        winner = grouped_list[0][i-1]
    else: 
        pass

print(f'Winner: {winner}')
print('__________________________')

#write output to results.txt
txt_path = os.path.join('analysis', 'results.txt')
with open(txt_path, 'w', newline='') as f: 
    f.write('Election Results\n'
        '__________________________\n'
        f'Total Votes: {total_votes}\n'
        '__________________________\n'
        f'{candidate_1}: {p1}% ({votes_1})\n{candidate_2}: {p2}% ({votes_2})\n{candidate_3}: {p3}% ({votes_3})\n{candidate_4}: {p4}% ({votes_4})\n'
        '__________________________\n'
        f'Winner: {winner}\n'
        '__________________________') 


