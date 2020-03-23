#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 11:10:50 2020

@author: thuyytruong
"""

President_file = open('Presidents.txt','r')
president=[]
parties=[]
for line in President_file:
    tmp_list = line.split(" ")
    president = tmp_list[0]
    parties = tmp_list[1:]
    Slice=tmp_list[2:]
    for each in Slice:
        tmp_list.append(int(each))
        
President_file.close()

data_file = open('BLS_private.csv','r')        
data_file= []
line_num = 1
for line in data_file:
    if line_num > 12:
        line = line.strip()
        tmp_list = line.split(',')
        data_file.append(tmp_list)
        line_num += 1
        
data_file.close()
