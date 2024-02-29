#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rishabh Saxena


Created on %(date)

File: %(file)

Description:
    
"""
from matplotlib import pyplot as plt

def main():
    f = open('rodents_311_2021.csv', 'r')
    neighborhood = []
    latitudes = []
    longitudes = []
    count = 0
    list_of_neighborhoods = []
    for line in f:
        #parsing the data
        nextline_block = line
        nextline_array = nextline_block.split(',')
        #check if blank neighborhood
        if line[0]==' ' or nextline_array.count('neighborhood')==1:
            continue
        if list_of_neighborhoods.count(nextline_array[0])<1:
            list_of_neighborhoods.append(nextline_array[0])
        #split into lists
        neighborhood.append(nextline_array[0])
        latitudes.append(float(nextline_array[1]))
        longitudes.append(float(nextline_array[2]))
        #keep count of total neighborhoods
        count +=1
    list_of_neighborhoods.sort()
    list_of_neighborhoods_nums = []
    for neigh in list_of_neighborhoods: 
        neighborhood_count=0
        for n in neighborhood:
            if n==neigh:
                neighborhood_count+=1
        list_of_neighborhoods_nums.append(neighborhood_count)
    #plotting
    plt.scatter(longitudes,latitudes, marker = ".", color = 'blue', label = 'Data' )
    plt.plot(-71.0892, 42.3398, marker ='o', color = 'red', label = 'Northeastern')
    plt.title("Latitude vs. Longitude Map of Rodent Reports in Boston 2021")
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.legend(['Data', 'Northeastern'])
    plt.savefig('boston_rodents.pdf', bbox_inches = 'tight')
    plt.show()
    #bar plotting
    plt.bar(list_of_neighborhoods, list_of_neighborhoods_nums,)
    plt.title("Rodent Report Comparison by Neighborhood")
    plt.xticks(rotation=90)
    plt.xlabel('Neighborhoods')
    plt.ylabel('Rodent Reports')
    plt.savefig('neighborhoods.pdf', bbox_inches = 'tight')
    plt.show
    #printing
    print ('Total number of rodent reports assigned to a valid neighborhood:', count)
    print ('Neighborhoods:')
    for n in list_of_neighborhoods:
        print(n)
    print ('Average number of rodent reports:', count/len(list_of_neighborhoods))
main()
    