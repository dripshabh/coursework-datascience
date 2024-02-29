"""
Rishabh Saxena
DS2000
Homework 5
October 16, 2022


File: exoplanets.py

Output for
generate_planet_report(find_most_similar_planet('Earth', PLANET_DATA),PLANET_DATA):
'The planet named  CFHTWIR-Oph 98 A b has a mass of 2479.542 Earth masses, a radius of 20.404200000000003 Earth radii, a period of 2936547288.0 days, a semimajoraxis of 200.0 AU, and a surface temperature of 1800.0 degrees K.'

Description:
    1. Identify the most Earth-like exoplanet using a method for measuring similarities and differences.
    2. Visualize the catalog of all discovered exoplanets and their properties to see how most newly discovered
    exoplanets are different from the Earth and are in fact more like “hot Jupiters”: Jupiter-sized planets orbiting
    close to their host star.
"""
def main():
    PLANET_DATA = read_data('exoplanets.csv')
    generate_planet_report(find_most_similar_planet('Earth', PLANET_DATA),PLANET_DATA)
    visualize_exoplanets(PLANET_DATA)

#read file and parse planet info
def read_data (file_name):
    planet_data_all = []
    f = open(file_name, 'r')
    for _ in f:
        if _[0] == '#':
            continue
        line_array = _.split(',')
        planet_data_per_planet=[]
        
        #names planet data
        planet_data_per_planet.append(line_array[0])
        
        #mass planet data store and convert to earth masses
        if line_array[2] == '':
            planet_data_per_planet.append(0.0)
        else:
            planet_data_per_planet.append(float(line_array[2])*317.89)
        
        #radius planet data store and convert to earth radii
        if line_array[3] == '':
            planet_data_per_planet.append(0.0)
        else:
            planet_data_per_planet.append(float(line_array[3])*10.97)
        
        #orbital period data store and convert to days
        if line_array[4] == '':
            planet_data_per_planet.append(0.0)
        else:
            planet_data_per_planet.append(float(line_array[4])*365.2422)
        
        #semimajoraxis data store
        if line_array[5] == '':
            planet_data_per_planet.append(0.0)
        else:
            planet_data_per_planet.append(float(line_array[5]))
        
        #surface temperature data store
        if line_array[11] == '':
            planet_data_per_planet.append(0.0)
        else:
            planet_data_per_planet.append(float(line_array[11]))
        planet_data_all.append(planet_data_per_planet)
    return (planet_data_all)
    f.close()

#find a specific planet by name in a dataset
def lookup_planet(planet_name, list_of_lists_planets):
    output=['There is no such planet in the list of data. The search is case sensitive!']
    for _ in list_of_lists_planets:
        if _[0] == planet_name:
            output=_
    return output

#find euclidean distance between two given planets
def euclidean_distance (planet_1_data, planet_2_data):
    quadrature_before_square_root = 0
    for i in range(5):
        quadrature_before_square_root += (float(planet_1_data[i+1]) - float(planet_2_data[i+1]))**2
    euclid = quadrature_before_square_root**0.5
    return euclid

#find most similar planet by smallest euclidean distance
def find_most_similar_planet(planet_name, list_of_lists_planets):
    smallest_euclidean_distance = euclidean_distance(lookup_planet(planet_name, list_of_lists_planets), list_of_lists_planets[0])
    smallest_euclidean_distance_name = ''
    for _ in list_of_lists_planets:
        if smallest_euclidean_distance < euclidean_distance(lookup_planet(planet_name, list_of_lists_planets), _):
            smallest_euclidean_distance = euclidean_distance(lookup_planet(planet_name, list_of_lists_planets), _)
            smallest_euclidean_distance_name= _[0]
    return smallest_euclidean_distance_name
    
#creates a human readable report of a planet with all of its relevant characteristics
def generate_planet_report(planet_name, list_of_lists_planets):
    planet_report_data = lookup_planet(planet_name, list_of_lists_planets)
    print ('The planet named ', str(planet_report_data[0]) + ' has a mass of', str(planet_report_data[1]) + ' Earth masses,', 'a radius of', str(planet_report_data[2]) + ' Earth radii,', 'a period of', str(planet_report_data[3]) + ' days,', 'a semimajoraxis of', str(planet_report_data[4]) + ' AU,', 'and a surface temperature of', str(planet_report_data[5]) + ' degrees K.')

#creates scatter plot graph visualization of planet data set
def visualize_exoplanets (planet_data):
    from matplotlib import pyplot as plt
    semimajoraxis_data = []
    mass_data = []
    earth_data = lookup_planet('Earth', planet_data)
    for _ in planet_data:
        mass_data.append(_[1])
        semimajoraxis_data.append(_[4])
    plt.scatter(mass_data,semimajoraxis_data, marker = ".", color = 'blue', label = 'Data' )
    plt.plot(earth_data[1], earth_data[4], marker ='x', color = 'red', label = 'Earth')
    plt.xscale('log') 
    plt.yscale('log')
    plt.title("Exoplanet Semimajor Axis data vs. Mass data")
    plt.xlabel('Exoplanet Mass')
    plt.ylabel('Exoplanet Semimajor Axis')
    plt.legend(['Exoplanet Data', 'Earth'])
    plt.savefig('exoplanet.png', bbox_inches = 'tight')
    plt.show()
    
main()
