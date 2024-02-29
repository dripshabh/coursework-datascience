'''
Rishabh Saxena
DS2000
Homework 5
November 14, 2022

Parses info from star wars script, creates a list of dictionaries in which each
dictionary contains line number, character, dialogue, and sentiment score of 
the dialogue and also creates a visualization of this informaiton for Luke and 
Leia specifically

Output:
Most positive line: 
character: BIGGS
line_number: 85
dialogue: I feel for you, Luke, you're going to have to learn what seems to be 
important or what really is important.  What good is all your uncle's work if 
it's taken over by the Empire?...  You know they're starting to nationalize 
commerce in the central systems...it won't be long before your uncle is merely 
a tenant, slaving for the greater glory of the Empire.
sentiment: 5 

Most negative line: 
character: LEIA
line_number: 270
dialogue: General Kenobi, years ago you served my father in the Clone Wars.  
Now he begs you to help him in his struggle against the Empire.  I regret that 
I am unable to present my father's request to you in person, but my ship has 
fallen under attack and I'm afraid my mission to bring you to Alderaan has 
failed.  I have placed information vital to the survival of the Rebellion into 
the memory systems of this R2 unit.  My father will know how to retrieve it.  
You must see this droid safely delivered to him on Alderaan.  This is our most 
desperate hour.  Help me, Obi-Wan Kenobi, you're my only hope.
sentiment: -6

DARTH VADER  ==> minimum: -2
DARTH VADER  ==> average: 0.06930693069306931
DARTH VADER  ==> maximum: 1
LEIA         ==> minimum: -6
LEIA         ==> average: 0.06930693069306931
LEIA         ==> maximum: 1
C3PO         ==> minimum: -3
C3PO         ==> average: 0.06930693069306931
C3PO         ==> maximum: 4
LUKE         ==> minimum: -2
LUKE         ==> average: 0.06930693069306931
LUKE         ==> maximum: 3
OBIWAN       ==> minimum: -3
OBIWAN       ==> average: 0.06930693069306931
OBIWAN       ==> maximum: 3
HAN SOLO     ==> minimum: -5
HAN SOLO     ==> average: 0.06930693069306931
HAN SOLO     ==> maximum: 5
'''

import matplotlib.pyplot as plt

PUNCTUATION = ['!', ''', '#', '$', '%', '&', ''', '(', ')', '*', '+', ',', '-',
               '.', '/', ':', ';','<', '=', '>', '?', '@', '[', ']', '^', '_',
               '`', '{', '}', '|', '~']

def read_data():
    '''
    reads starwars.txt file into a list of dictionaries
    
    Parameters
    ----------
    None

    Returns
    -------
    star_wars_data, a list of dictionaries, in each dictionary there is a line,
    name, and dialogue

    '''
    
    star_wars_data = []
    file = open('starwars.txt', 'r')
    for line in file:
        if line [0:1] == 'l':
            continue
        temp_dict = {}
        line_split = line.split('|')
        temp_dict ['line_number'] = line_split[0]
        temp_dict ['character'] = line_split[1]
        temp_dict ['dialogue'] = line_split [2]
        star_wars_data.append(temp_dict)
    file.close()
    return (star_wars_data)

def read_words(file_name):
    '''
    reads positive-words.txt or negative-words.txt files into lists of words
    
    Parameters
    ----------
    file_name, a string of the file name

    Returns
    -------
    list_of_words, a list of strings, each string is a word

    '''
    file = open(file_name)
    list_of_words = [line.rstrip() for line in file.readlines()]
    return list_of_words

def calculate_sentiment(dictionary, pos, neg):
    '''
    calculates sentiment of dialogue value of dictionary

    Parameters
    ----------
    dictionary: dictionary
        dictionary containing line number, character, dialogue values
    pos : list of strings
        positive words
    negative : list of strings
        negative words

    Returns
    -------
    sentiment: int
        sentiment score

    '''
    sentiment = 0
    dialogue = dictionary['dialogue']
    for word in dialogue.split():
        punc = ''.join(PUNCTUATION)
        word = word.rstrip(punc).lower()
        if word in pos:
            sentiment += 1
        if word in neg:
            sentiment -= 1
    return sentiment
    
    
def add_sentiment_to_list_of_dictionaries(data):
    '''
    adds sentiment to each dictionary in list of dictionaries based on value 
    for 'dialogue' key
    
    Parameters
    ----------
    data, list of dictionaries, presumably have values for 'dialogue' key

    Returns
    -------
    updated_data, list of dictionaries, added sentiment key per dictionary with
    sentiment score based on 'dialogue' value

    '''
    pos = read_words('positive-words.txt')
    neg = read_words('negative-words.txt')
    updated_data = data
    for dictionary in updated_data:
        sentiment = calculate_sentiment(dictionary, pos, neg)
        dictionary['sentiment'] = sentiment
    return updated_data

def calculate_extreme_sentiment(data):
    '''
    a
    
    Parameters
    ----------
    data, a list of dictionaries, in each dictionary there is a line, name, 
    dialogue, and sentiment

    Returns
    -------
    
    '''
    maxSentiment = max(data, key = lambda x:x['sentiment'])
    minSentiment = min(data, key = lambda x:x['sentiment'])
    return [maxSentiment, minSentiment] 

def generate_sentiment_report(dictionaries):
    '''
    generates report detailing max and min sentiment lines

    Parameters
    ----------
    dictionaries: list
        contains maxi and mini dictionaries

    Returns
    -------
    None.

    '''
    maxi = dictionaries[0]
    mini = dictionaries[1]
        
    print ('Most positive line: \n'+ 
           'character:', maxi['character'] + '\n'
           'line_number:', maxi['line_number'] + '\n' +
           'dialogue:', maxi['dialogue'] +
           'sentiment:', maxi['sentiment'], '\n')
    
    print ('Most negative line: \n'+ 
           'character:', mini['character'] + '\n'
           'line_number:', mini['line_number'] + '\n' +
           'dialogue:', mini['dialogue'] +
           'sentiment:', mini['sentiment'])
def generate_sentiment_report_info_per_character (data, character):
    '''
    

    Parameters
    ----------
    data, a list of dictionaries, in each dictionary there is a line, name, 
        dialogue, and sentiment
    
    character, a string, character code that identifies which character this
        function is being called on

    Returns
    -------
    sentiment_list_per_character, a list of integers and a string, contains the
        [minimum, average, maximum, character] sentiment for the called character
    '''
    sum_of_sent = 0
    count = 0
    lst_dialogue_per_character = []
    for dictionary in data:
        if dictionary['character'] == character:
            lst_dialogue_per_character.append(dictionary)
        sum_of_sent += dictionary['sentiment']
        count += 1
    maximum = max(lst_dialogue_per_character, key = lambda x:x['sentiment'])
    minimum = min(lst_dialogue_per_character, key = lambda x:x['sentiment'])
    average = sum_of_sent/count
    return [minimum['sentiment'], average, maximum['sentiment'], character]

def generate_sentiment_table (data):
    '''
    creates a table given the dataset from create_chardata
    
    parameters:
    data: a list of dictionaries, all of the lines to calculate the sentiment
    score for.
    
    
    returns:
    none.
    '''
    for char in ['DARTH VADER', 'LEIA', 'C3PO', 'LUKE', 'OBIWAN', 'HAN SOLO']:
        char_info_list = generate_sentiment_report_info_per_character(data, char)
        print(f'{char:12} ==> minimum:', char_info_list[0])
        print(f'{char:12} ==> average:', char_info_list[1])
        print(f'{char:12} ==> maximum:', char_info_list[2])
def generate_sentiment_list_per_character (data, character):
    '''
    Parameters
    ----------
    data, a list of dictionaries, in each dictionary there is a line, name, 
        dialogue, and sentiment
    
    character, a string, character code that identifies which character this
        function is being called on

    Returns
    -------
    lst_sentiment_per_character, all sentiment values, in order for dialogue
        [minimum, average, maximum, character] sentiment for the called character
    '''
    lst_sentiment_per_character = []
    for dictionary in data:
        if dictionary['character'] == character:
            lst_sentiment_per_character.append(dictionary['sentiment'])
    return lst_sentiment_per_character

def create_barplot(data):
    '''
    creates a barplot comparing the sentiment scores of Luke and Leia
    
    parameters:
    
    data: a list of dictionaries, all of the lines to calculate the sentiment
    score for.
    
    positive: a list of strings, all of the positive words
    
    negative: a list of strings, all of the negative words
    
    returns:
    none.
    '''
    data_list_luke = generate_sentiment_list_per_character(data, 'LUKE')
    data_list_leia = generate_sentiment_list_per_character(data, 'LEIA')
    plt.hist(data_list_luke, bins=10, alpha=0.5, color = 'blue')
    plt.hist(data_list_leia, bins=10, alpha=0.5, color = 'red')
    plt.ylabel('Frequency')
    plt.title('Luke\'s(blue) vs. Leia\'s(red) sentiment scores')
    plt.savefig('luke_leia.pdf')
    plt.show()
def avg(L):
    ''' Compute the numerical average of a list of numbers.
    If list is empty, return 0.0 '''
    if len(L) > 0:
        return sum(L) / len(L)
    else:
        return 0.0
    
def get_window(L, idx, window_size=20):
    ''' Extract a window of values of specified size
    centered on the specified index
    L: List of values
    idx: Center index
    window_size: window size
    '''
    minrange = max(idx - window_size // 2, 0)
    maxrange = idx + window_size // 2 + (window_size % 2)
    return L[minrange:maxrange]

def moving_average(L, window_size=20):
    ''' Compute a moving average over the list L
    using the specified window size
    L: List of values
    window_size - The window size (default=1)
    return - A new list with smoothed values
    '''
    mavg = []
    for i in range(len(L)):
        window = get_window(L, i, window_size)
        mavg.append(avg(window))
    return mavg
def generate_sentiment_list (data):
    '''
    creates a list of all sentiments throughout the movie
    
    parameters:
    data: a list of dictionaries, all of the lines to calculate the sentiment
    score for.
    returns:
    lst_of_sentiments: a list of all sentiment values
    '''
    lst_of_sentiments = []
    for elem in data:
        lst_of_sentiments.append(elem['sentiment'])
    return lst_of_sentiments
def plot_avg(data):
    '''
    plots a moving average of the sentiment scores of the star wars movie's dialogues
    
    parameters:
    data: a list of dictionaries, all of the lines to calculate the sentiment
    score for.
    '''
    plt.plot(range(1, 1011), moving_average(generate_sentiment_list(data)),
             label = 'running average')
    tarkin_ycoord = min(moving_average(generate_sentiment_list(data)))
    attack_ycoord = max(moving_average(generate_sentiment_list(data)))
    plt.plot(281, tarkin_ycoord, marker = '.', color = 'red')
    plt.text(289, tarkin_ycoord, 'Tarkin\'s Conference')
    plt.plot(830, attack_ycoord, marker = '.', color = 'green')
    plt.text(828, attack_ycoord, 'Attack!')
    plt.ylabel('Sentiment score')
    plt.xlabel('Line number')
    plt.title('Moving Average of Sentiment Score over Star Wars Movie')
    plt.savefig('story_arc.pdf')
    plt.show()
    
def char_sentiment_count(data):
    '''
    calculates the total number of positive and negative lines spoken and stores
    it in a dictionary.
    
    parameters:
    dataset: a list of dictionaries, all of the lines to calculate the sentiment
    score for.
    
    returns:
    character_sentiment_dictionry: a dictionary that contains first the character name then a list,
    where the first value is the positive score and the second value is the negative.
    '''
    
    # loading in the list of scores:
    scorelist = generate_sentiment_list(data)
    # creating an empty dictionary to later store values in
    character_sentiment_dictionary = {}
    # goes through every line in dataset
    for line in data:
        # appending values if the character is already in the dictionary.
        if line['character'] in character_sentiment_dictionary:
            if scorelist[data.index(line)] > 0:
                # increasing the positive score by 1 if line is positive
                character_sentiment_dictionary[line['character']][0] += 1
            if scorelist[data.index(line)] < 0:
                # increasing the negative score by 1 if line is negative
                character_sentiment_dictionary[line['character']][1] += 1
        # creating a new key and corresponding value if the character is NOT in dict.
        if line['character'] not in character_sentiment_dictionary:
            if scorelist[data.index(line)] > 0:
                # creating the new value, starting with 1 positive score
                character_sentiment_dictionary[line['character']] = [1, 0]
            if scorelist[data.index(line)] < 0:
                # creating the new value, starting with 1 negative score
                character_sentiment_dictionary[line['character']] = [0, 1]
    return character_sentiment_dictionary

def plot_character_information(data):
    '''
    plots a scatterplot of all major character's total negative lines vs.
    total positive lines
    
    parameters:
    data: a list of dictionaries, all of the lines to calculate the sentiment
    score for.
    
    returns:
    none.
    '''
    char_sentiment_dictionary = char_sentiment_count(data)
    lst_legend = []
    for char in char_sentiment_dictionary:
        if char_sentiment_dictionary[char][0] + char_sentiment_dictionary[char][1] > 10:
            plt.scatter(char_sentiment_dictionary[char][1], char_sentiment_dictionary[char][0])
            lst_legend.append(char)
    plt.legend(lst_legend, title = 'Characters', fontsize = 7)
    plt.xlim(0, 70)
    plt.ylim(0, 70)
    plt.plot([0, 70], [0, 70], linestyle = 'dashed', color= 'red')
    plt.xlabel('Number of Negative Lines')
    plt.ylabel('Number of Positive Lines')
    plt.title('Number of Negative Lines vs. Number of Positive Lines')
    plt.savefig('character_scores.pdf')
    plt.show()

def main():
    star_wars_data = read_data()
    
    data_with_sentiment = add_sentiment_to_list_of_dictionaries(star_wars_data)
    
    generate_sentiment_report(calculate_extreme_sentiment(data_with_sentiment))
    
    generate_sentiment_table(data_with_sentiment)
    
    create_barplot(data_with_sentiment)
    
    plot_avg(data_with_sentiment)
    
    plot_character_information(data_with_sentiment)
    
if __name__ == '__main__':
    main()