#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: thuyytruong
"""
'''employmentData = open("TotalPrivateEmployment-data.csv", "r") #data file and program are in same directory4
lineList = [line.rstrip('\n') for line in open("TotalPrivateEmployment-data.csv")]
'''
import csv
with open('TotalPrivateEmployment-data.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(row)
        line_count += 1
    print(f'Processed {line_count} lines.')

def main():
    President_file = open('Presidents.txt','r')
    president=[]
    parties=[]
    for line in President_file:
        tmp_list = line.split("\n")
        president = tmp_list[0]
        parties = tmp_list[1:]
        Slice=tmp_list[2:]
        for each in Slice:
            tmp_list.append(each)
            return president, parties
        
        President_file.close()

   
    Data_file= open ('TotalPrivateEmployment-data.cvs','r')
    data=[]
    line_num = 1
    for line in Data_file:
        if line_num > 12:
            line = line.strip()
            tmp_list = line.split(',')
            data.append(tmp_list)
        line_num +=1
    return data
    
csv_file.close()

def Get_totals(Data,Presidents):
   
    Output = []
    PreOutput = {}
    for i in Data:
        i[0] = int(i[0])
        try:
            PreOutput[Presidents[i[0]-1]].append(i[1])
            PreOutput[Presidents[i[0]]].extend(i[1:])
        except KeyError:
            PreOutput[Presidents[i[0]]] = []
            PreOutput[Presidents[i[0]]].extend(i[1:])
    for i in PreOutput:
        k = PreOutput[i]
        Tmp_list = [i]
        Before = int(k[0])
        total = 0
        for j in k:
            if j == '':
                continue
            j = int(j)
            total += j -Before
            Before = j
        Tmp_list.append(total)
        Output.append(Tmp_list)
    return Output

def Print_output(Output,Parties):
  
    Rep_total = 0
    Dem_total = 0
    print("Republicans:")
    for i in Output:
        if Parties[i[0]] == "Republican":
            Rep_total += i[1]
            if i[1] > 0:
                print(i[0], ":",abs(round(i[1]/1000,1)), "Million created jobs")
            else:
                print(i[0], ":",abs(round(i[1]/1000,1)), "Millon lost jobs")

    print("\nTotal jobs created:", abs(round(Rep_total/1000,1)), "Million jobs" )
    print("\n----------\n")
    print("Democrats:")
    for i in Output:
        if Parties[i[0]] == "Democrat":
            Dem_total += i[1]
            if i[1] > 0:
                print(i[0], ":",abs(round(i[1]/1000,1)), "Million created jobs")
            else:
                print(i[0], ":",abs(round(i[1]/1000,1)), "Million lost jobs")
    print("\nTotal jobs created:", abs(round(Dem_total/1000,1)), "Million jobs" )
    print("\n----------\n")
    print("The numbers overall are accurate but the individual numbers are off because of terms ending too soon.")
    print("This data show that while president clinton's numbers were off, his point still stands.")

  

