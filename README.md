# python-challenge
Python Challenge
# IMPORTANT NOTE
## In order to get the unique names of each candidate we used the set() function in python which returns the unique names of the candidates... this method gives the names in a different order each time the script is interpreted... thus the results.txt file has to be updated each time the anaysis is run.. but the script will always match the proper candidate to the number and percentage of votes and give the correct winner.

## Background
This repository consists of analyses done for two separate challenges: PyBank and pyPoll 

## PyBank
* In this challenge, I wrote a Python script for analyzing the financial records of a company in [budget_data.csv](PyBank/Resources/budget_data.csv). 
* The Python script calculates and gives each of the following:

  * The total number of months included in the dataset
 
  * The net total amount of "Profit/Losses" over the entire period

  * The average of the changes in "Profit/Losses" over the entire period

  * The greatest increase in profits (date and amount) over the entire period

  * The greatest decrease in losses (date and amount) over the entire period

* In addition, the results of the script print to the analysis.txt file in pyBank/analysis/

## PyPoll

* In this challenge I wrote a python script to analyze a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv).
The analysis gives: 

  * The total number of votes cast

  * A complete list of candidates who received votes

  * The percentage of votes each candidate won

  * The total number of votes each candidate won

  * The winner of the election based on popular vote.

* In addition, the python script print the analysis to the terminal and exports a text file with the results (pyPoll/analysis/results.txt) 



