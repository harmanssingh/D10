#!/usr/bin/env python3# Exercise: Presidents# Author GitHub usernames:# #1:# #2:# Instructions:# Write a program to:# (1) Load the data from presidents.txt into a dictionary.def load_data():    with open('presidents.txt', 'r') as f:        txt=f.readlines()    d={}    for lines in txt:        splitline=lines.strip().split(',')        if 'None' in splitline[2]:            d[splitline[0]]=(splitline[1],'2016')        else:            d[splitline[0]]=(splitline[1],splitline[2])    dyears={}    for years in range(1732, 2017):        presidents=[]        n=0        for keys in d:            if int(d[keys][0]) <= years <=int(d[keys][1]):                n+=1                presidents.append(keys)        dyears[years] = (n,presidents)    min_tuple=min_year(dyears)    str_min=','.join(min_tuple[1])    least='Least = {}\n{}'.format(repr(min_tuple[0]),repr(str_min))    print(least)    max_tuple=max_year(dyears)    str_max=','.join(max_tuple[1])    most='Most = {}\n{}'.format(repr(max_tuple[0]),repr(str_max))    print(most)    with open('presidentsout.txt','w') as f:        f.write(least+'\n')        f.write(most)def min_year(dict):    min_year=1732    min_val=100000    min_presidents=[]    for keys in dict:        if dict[keys][0] <= min_val:            min_year=keys            min_val=dict[keys][0]            min_presidents=dict[keys][1]    return min_year,min_presidentsdef max_year(dict):    max_year=1732    max_val=0    max_presidents=[]    for keys in dict:        if dict[keys][0] >= max_val:            max_year=keys            max_val=dict[keys][0]            max_presidents=dict[keys][1]    return max_year,max_presidents# (2) Print the years the greatest and least number of presidents were alive.#     (between 1732 and 2016 (inclusive))#     Ex.#       'least = 2015'#       'John Doe'#       'most = 2015'#       'John Doe, Jane Doe, John Adams, and Jane Adams'# Bonus: Confirm there are no ties. If there is a tie print like so:#     Ex.#       'least = 1900, 2013-2015'#       'John Doe (1900)'#       'Jane Doe (2013-2015)'#       'most = 1900-1934, 2013'#       'John Doe, Jane Doe, John Adams, and Jane Adams (1900-1933)'#       'Sally Doe, Billy Doe, Mary Doe, and Cary Doe (1934)'#       'Alice Doe, Bob Doe, Zane Doe, and Yi Do (2013)'# (3) Write your print statements to a file (greatest_least.txt) as well.# Upload that file as well.############################################################################### Imports# Body##############################################################################def main():  # CALL YOUR FUNCTION BELOW    ...    load_data()if __name__ == '__main__':    main()