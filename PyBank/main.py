
import os 
import csv 

#import the csv data 
filepath = os.path.join('Resources', 'budget_data.csv')
#print(filepath)

with open(filepath) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)

    #Turn iterable into a list 
    bank_data = list(csvreader)
    
# Your task is to create a Python script that analyzes the records to calculate each of the following:

# The total number of months included in the dataset
    #The total number of months will be equal to the number of rows in the dataset minus 1 for the header 
length = len(bank_data)
number_months = (length-1)
print('Financial Analysis')
print('_________________________')
print(f'Total Months: {number_months}')

# The net total amount of "Profit/Losses" over the entire period
net = 0
for i in range(number_months):  
    net = net + int(bank_data[i+1][1])
print(f'Total: ${net}')
#print(bank_data[2][1])

# The average of the changes in "Profit/Losses" over the entire period
monthly_change = 0 
total_change = 0 
for i in range(number_months -1):  
    monthly_change = monthly_change + (int(bank_data[i+2][1]) - int(bank_data[i+1][1]))
    total_change = total_change + monthly_change
    #print(monthly_change)
    monthly_change = 0
average_change = round((total_change/ (number_months -1 )), 2 )
print(f'Average Change: ${average_change}')



# The greatest increase in profits (date and amount) over the entire period
#Before using max() function to find the greatest change period in our list lets add the monthly change data to the list 'bank_data'
for i in range(number_months -1):  
    monthly_change = monthly_change + (int(bank_data[i+2][1]) - int(bank_data[i+1][1]))
    #print(monthly_change)
    bank_data[i+2].append(monthly_change)
    monthly_change = 0

#Fill missing data with a zero 
bank_data[0].append(0) 
bank_data[1].append(0)

#Find Max and Min values using tuple and *zip method
cleaned_data = list(zip(*bank_data))
greatest_increase = max(cleaned_data[2])
greatest_decrease = min(cleaned_data[2])

#print(cleaned_data)
# Match the max and min values with the date in which they occurred 
#First find which data to loop through the easiest bank_data or cleaned_data 
#checking indexes on each 
    # print(cleaned_data[2][2])
    # print(bank_data[2][2])
    # print(type(cleaned_data[2][2]))
    # print(type(bank_data[2][2]))
    # print(bank_data[0:3]) #the result shows it doesn't matter which data you want to loop through either one's index works the same                                                                                                                                                                                                                                                                                                                                                                                    
date_greatest_increase = str()
date_greatest_decrease = str()
for i in range(number_months -1):
    if cleaned_data[2][i+1] == greatest_increase : 
        date_greatest_increase = cleaned_data[0][i+1]
    else:
        pass

for i in range(number_months -1):
    if cleaned_data[2][i+1] == greatest_decrease : 
        date_greatest_decrease = cleaned_data[0][i+1]
    else:
        pass
print(f'greatest increase: {date_greatest_increase} ${greatest_increase}')
print(f'greatest decrease: {date_greatest_decrease} ${greatest_decrease}')


#write results to text file called 'financial_analysis.txt' 
txt_path = os.path.join('analysis', 'financial_analysis.txt')

with open(txt_path, 'w', newline='') as f: 
    f.write('Financial Analysis\n'
    '_______________________\n'
    f'Total Months: {number_months}\n'
    f'Total: ${net}\n'
    f'Average Change: ${average_change}\n'
    f'greatest increase: {date_greatest_increase} ${greatest_increase}\n'
    f'greatest decrease: {date_greatest_decrease} ${greatest_decrease}') 

