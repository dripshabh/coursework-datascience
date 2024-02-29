""" Rishabh Saxena
    DS2000
    Homework 7
    November 6, 2022


    File: bluebikes.py

    Description:
        1. Read blue bikes data
        2. Generate data report
    Output:
    Number of trips ending at Forsyth St at Huntington Ave:
    Friday : 481
    Saturday : 230
    Sunday : 219
    Monday : 250
    Tuesday : 314
    Wednesday : 296
    Thursday : 277
"""
import matplotlib.pyplot as plt


def read_data ():
    #reads trips.csv file into a list of dictionaries
    #no parameters
    #returns a list of dictionaries
    data = []
    headerlist = ["duration", "start_day", "start_day_name", "start_station",
                  "end_station", "bike_id"]
    file = open("trips.csv", "r")
    file.readline()
    for line in file:
        line = line.split(",")
        rowdict = {}
        for i in range(len(line)):
            if "\n" in line[i]:
                rowdict.update({headerlist[i]: line[i].replace("\n", "")})
            else:
                rowdict.update({headerlist[i]: line[i].replace("\n", "")})
        data.append(rowdict)
    return data
    file.close()


def read_stations():
    #reads stations.csv file into a separate dictionary
    #no parameters
    #returns dictionary containg station information
    data = {}
    file = open ('stations.csv', 'r')
    file.readline()
    for line in file:
        line = line.split(',')
        line[2]= line[2][:-1]
        data[line[0]] = [float(line[1]),float(line[2])]
    return data

import math

#Earth radius average
EARTH_RADIUS_MILES = 3959
def haversine_distance(start, end):
    #calculates distance between two points on earth
    #parameters are starting point, a list of two floats, and an ending point, a list of two floats
    #returns distance as a float
    """
    Calculates the distance in miles between two points on the Earth's surface 
    described by latitude and longitude.
    Parameters:
    start: list
    list of two floats—latitude and longitude
    end: list
    list of two floats—latitude and longitude
    Return:
    float - distance in miles between the two points
    """
    lat1 = start[0]
    long1 = start[1]
    lat2 = end[0]
    long2 = end[1]
    lat1 = math.radians(lat1)
    long1 = math.radians(long1)
    lat2 = math.radians(lat2)
    long2 = math.radians(long2)
    delta_lat = lat2 - lat1
    delta_long = long2 - long1
    # the earth's radius is a constant value
    a = math.sin(delta_lat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(delta_long / 2)**2
    haversine = EARTH_RADIUS_MILES * 2 * math.asin(math.sqrt(a))
    return haversine

def alter_data():
    #calculates speed and distance of each atrip, and adds these variables to the list of dictionaries
    #no parameters
    #returns triplist, a list of dictionaries of all trips
    trip_list = read_data()
    station_list = read_stations()
    for trip in trip_list:
        if trip['start_station'] not in station_list or trip['end_station'] not in station_list:
            distdict = dict({"dist": "N/A"})
            speeddict = dict({"mph": "N/A"})
        elif trip['start_station'] in station_list and trip['end_station'] in station_list:
            start = station_list[trip['start_station']]
            end = station_list[trip['end_station']]
            distance = haversine_distance(start, end)
            distdict = dict({"dist": distance})
            speed = distance / (float(trip["duration"]) / 3600)
            speeddict = dict({"mph": speed})
        else:
            pass
        trip.update(speeddict)
        trip.update(distdict)
    return trip_list
    print (trip_list[0:3])
    
def col_extract(key):

    # Extracts a column from the list of dictionaries produced by alter_data
    # Parameters:
    # key: string, the desired key to be extracted
    # Returns:
    # col: a list of values from the desired keys
    col = []
    triplist = alter_data()
    for trip in triplist:
        if trip[key] != "N/A":
            col.append(trip[key])
    return col

def make_hist():
    # Creates two histograms, one for mph and one for distance values
    
    # Parameters:
    # none
    
    # Returns:
    # none
    plt.hist(col_extract("dist"), bins = 100, edgecolor='blue')
    plt.ylabel("Frequency")
    plt.xlabel("Distance (miles)")
    plt.title("Occurences of Distances in Blue Bike Trips")
    plt.savefig("distances.pdf")
    plt.show()
    plt.hist(col_extract("mph"), bins = 100, edgecolor="blue")
    plt.ylabel("Frequency")
    plt.xlabel("Speed (mph)")
    plt.title("Occurences of Speeds in Blue Bike Trips")
    plt.savefig("speeds.pdf")
    plt.show()

def daycount():
    # Creates a dictionary that maps day of the week to the count of trips that
    # end at the forsyth st. station. Prints these counts

    triplist = alter_data()
    forsyth_list = []
    for trip in triplist:
        if trip["end_station"] == "Forsyth St at Huntington Ave":
            forsyth_list.append(trip)
    daydict = {}
    for trip in forsyth_list:
        if trip["start_day_name"] not in daydict:
            daydict.update(dict({trip["start_day_name"]: 1}))
        else:
            daydict[trip["start_day_name"]] += 1
    print("Number of trips ending at Forsyth St at Huntington Ave:")
    for key in daydict:
        print(key + " :", daydict[key])
        
def main():
    make_hist()
    
    daycount()

if __name__ == "__main__":
    main()
