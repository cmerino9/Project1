# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 08:43:34 2020

@authors: Cortney, Thuy, Shireen, Kazi
"""
import csv

def jobsData(demYears,democraticJobs,repYears,republicanJobs):
    with open('BLS_private.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for line in csv_reader:
            year = line[0]
#            print(line,year,total)
            if year in demYears:
                democraticJobs.extend(line[1:13]) #adds to the list of jobs, each month
            elif year in repYears:
                republicanJobs.extend(line[1:13]) #adds to the list of jobs, each month
        return democraticJobs, republicanJobs
    csv_file.close()

def presidentInfo(demYears, repYears):        
    President_file = open('Presidents.txt','r')
#    president = []
    party = []
    termServed = []
    totalDemocrats = 0
    totalRepublicans = 0
    with open("Presidents.txt", "r") as President_file:
        csv_reader = csv.reader(President_file, delimiter=',')
        for line in csv_reader:
#            president = line[0] #First column is the president's name
            party = line[1] #second column is the party affiliation
            termServed = line[2:] #look into split termserved= line.split(',')
            if party == 'Democrat':
                totalDemocrats += 1
                demYears.extend(termServed) #add list of years each Democratic president served to total years Democrats were in office
            elif party == 'Republican':
                totalRepublicans += 1
                repYears.extend(termServed) #add list of years each Republican president served to total years Republicans were in office
        print("From 1961 to 2019, there were", totalDemocrats, "Democrats that served a total of", len(demYears), "years, and", totalRepublicans, "Republicans that served a total of", len(repYears), "years.")
        return demYears, repYears
                   
    President_file.close()          

demYears = []
repYears = []
democraticJobs = []
republicanJobs = []
totalDemocraticJobs = 0
totalRepublicanJobs = 0
demYears, repYears = presidentInfo(demYears,repYears) #unpacks 2 returned lists into separate variables
democraticJobs, republicanJobs = jobsData(demYears,democraticJobs,repYears,republicanJobs)
democraticJobs = [ int(x) for x in democraticJobs ] #converts each item in list to integers
republicanJobs = [ int(x) for x in republicanJobs ] #converts each item in list to integers
for each in democraticJobs:
    totalDemocraticJobs += each #iterate through list and add each month to total Democratic jobs
for each in republicanJobs: 
    totalRepublicanJobs += each #iterate through list and add each month to total Republican jobs
totalJobs = (totalDemocraticJobs + totalRepublicanJobs) // 1000000 #converts into million
print("The Democrats produced", totalDemocraticJobs, "jobs, and the Republicans produced", totalRepublicanJobs, "jobs for a total of about", totalJobs, "million.")
print("\nIf we take the average jobs per year for both parties (to factor the difference between time for each party held in office), it comes out to about", totalDemocraticJobs // len(demYears), "for Democrats and", totalRepublicanJobs // len(repYears), "for Republicans. That is a pretty small difference.")
print("We can conclude that President Bill Clinton might have been right at the time (even though his actual numbers seem to be off) but since 1961, \"jobs produced\" has remained somewhat even between the parties.")
