""" Rishabh Saxena
    DS2000
    Homework 6
    October 16, 2022


    File: heart_explore.py

    Description:
        1. Read heart disease date
        2. Answer questions based off the data
        3. Generate a plot to visualize the data
    Output for generate_heart_data_report:
        
    Number of patients: 918 
    Number of patients with heart disease: 508 
    Average age: 53.5 years
    Average age of patients with heart disease: 55.9 years 
    Average resting blood pressure: 132.4 mmHg 
    Average resting blood pressure of partients with heart disease: 134.2 mmHg 
"""
from matplotlib import pyplot as plt

#read file and parse heart data into list of lists with 7 attributes (Age, Sex Assigned at Birth, Type of Chest Pain, BP, Cholesterol level, HR, HD)
def read_data (file_name):
    heart_data_all = []
    f = open(file_name, 'r')
    
    #looping though line-by-line, skipping first line, and splitting each line by comma
    for _ in f:
        if _[0] == 'A':
            continue
        line_array = _.split(',')
        
        #int casting numeric elements
        for i in [0,3,4,5]:
            line_array[i] = int(line_array[i])
        line_array[6] = int(line_array[6][0])
        
        heart_data_all.append(line_array)
    return(heart_data_all)
    f.close()

#find age and bp averages of all patients vs. those with heart disease
def generate_heart_data_report(heart_data_list_of_lists):
    #setting up all relevant variables for questions
    count = 0
    count_heart_disease = 0
    age_total = 0
    age_total_heart_disease = 0
    blood_pressure_total = 0
    blood_pressure_total_heart_disease = 0
    
    #looping through and incrementing as neccessary to answer all questions
    for _ in heart_data_list_of_lists:
        count += 1
        age_total += _[0]
        blood_pressure_total += _[3]
        if _[6] == 1:
            count_heart_disease += 1
            age_total_heart_disease += _[0]
            blood_pressure_total_heart_disease += _[3]
    
    #printing values and rounding the averages to 1 decimal
    print (
        'Number of patients:',count,'\n'+
        'Number of patients with heart disease:', count_heart_disease, '\n' +
        'Average age:', round(age_total/count,1), 'years\n' +
        'Average age of patients with heart disease:', round(age_total_heart_disease/count_heart_disease,1), 'years \n' +
        'Average resting blood pressure:', round(blood_pressure_total/count, 1), 'mmHg \n'+
        'Average resting blood pressure of partients with heart disease:', round(blood_pressure_total_heart_disease/count_heart_disease,1), 'mmHg \n'
        )

def generate_heart_data_scatterplot (heart_data_list_of_lists):
    maximum_hr = []
    cholesterol = []
    colors = []
    for _ in heart_data_list_of_lists:
        maximum_hr.append(_[5])
        cholesterol.append(_[4])
        if _[6] == 1:
            colors.append('r')
        else:
            colors.append('b')
    plt.scatter(maximum_hr, cholesterol, marker = '.', color=colors)
    plt.title("Cholesteral vs. Maximum Heart Rate, sorted by Heart Disease")
    plt.xlabel('Maximum Heart Rate')
    plt.ylabel('Cholesterol')  
    plt.savefig('heart.png', bbox_inches = 'tight')      

def main():
    HEART_DATA = read_data('heart.csv')
    generate_heart_data_report(HEART_DATA)
    generate_heart_data_scatterplot(HEART_DATA)

if __name__ == "__main__":
    main()