# 663eb3f5210040b8ed1e8674

""" 
A student wants to find the top 3 most common words in two separate but similar statements: 
“I love learning and teaching, teaching is fun and learning is even more fun!” 
and “I love teaching and learning, learning is fun and teaching is even more fun!”. 
To do this, first separate the sentences and then take the union of the unique words contained in both statements. 
Next, to determine the frequency of each word within the two statements, count the occurrence of every word within the union. 
Finally, identify the top 3 most frequent words in the two statements, 
then calculate and provide the total count of all words within the two statements' union.


1. Use pythoninterpreter to get the 3 most common words and their frequency
defining two lists and gettting the union of all the words in the list for sentence A and the list for sentence B. 
Sentence A: “I love learning and teaching, teaching is fun and learning is even more fun!”. 
Sentence B: “I love teaching and learning, learning is fun and teaching is even more fun!”

2. Use pythoninterpreter to determine the frequency of each word from previous step




Separate the sentences:
Use the pythoninterpreter tool to separate the sentences into individual words.
Take the union of the unique words:
Use the pythoninterpreter tool to find the union of the unique words from both statements.
Count the occurrence of every word:
Use the pythoninterpreter tool to count the occurrence of every word within the union.
Identify the top 3 most frequent words:
Use the pythoninterpreter tool to sort the words by frequency and to select the top 3 words from the sorted list.
Calculate the total count of all words:
Use the pythoninterpreter tool to add up the counts for all words in the union.
Use the pythoninterpreter tool to verify the total count.



1.    Separate the sentences:

Use the pythoninterpreter tool to separate the sentences into individual words.

2.    Take the union of the unique words:

Use the pythoninterpreter tool to find the union of the unique words from both statements.

3.    Count the occurrence of every word:

Use the pythoninterpreter tool to count the occurrence of every word within the union.

4.    Identify the top 3 most frequent words:

Use the pythoninterpreter tool to sort the words by frequency and to select the top 3 words from the sorted list.

5.    Calculate the total count of all words:

Use the pythoninterpreter tool to add up the counts for all words in the union.

Use the pythoninterpreter tool to verify the total count.





1.    Separate the sentences:

Use the wolfram_alpha tool to separate the sentences into individual words.

Use the wiki_search tool to search for the phrases and retrieve the individual words from the search results.

2.    Take the union of the unique words:

Use the calculator tool to find the union of the unique words from both statements.

Use the wolfram_alpha tool to perform set operations on the unique words.

3.    Count the occurrence of every word:

Use the wolfram_alpha tool to count the occurrence of every word within the union.

Use the calculator tool to add up the counts for each word.

4.    Identify the top 3 most frequent words:

Use the wolfram_alpha tool to sort the words by frequency.

Use the calculator tool to select the top 3 words from the sorted list.

5.    Calculate the total count of all words:

Use the calculator tool to add up the counts for all words in the union.

Use the wolfram_alpha tool to verify the total count.
 """

#1

words_a = str("I love learning and teaching, teaching is fun and learning is even more fun!").lower().split()
words_b = str("I love teaching and learning, learning is fun and teaching is even more fun!").lower().split()

for i in range(len(words_a)):
    words_a[i] = ''.join(letter for letter in words_a[i] if letter.isalpha())

for i in range(len(words_b)):
    words_b[i] = ''.join(letter for letter in words_b[i] if letter.isalpha())

union_words = [value for value in words_a if value in words_b]

word_frequency = {}

for word in union_words:
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

max_count = max(word_frequency.values())

top_3_common ={}

for k, v in word_frequency.items():
    if v == max_count:
        top_3_common.update({k : v})
        if len(top_3_common) == 3:
            break

print(top_3_common)




'''

What are the two consecutive prime numbers that are smaller than 100 whose perfect square 
integers have the largest possible integer as the absolute value of their difference and what is the value of this largest integer?


1. Using wolfram_alpha identify Prime Numbers Below 100 but closer to 100
2. Using wolfram_alpha identify Consecutive Prime Pairs from step 1
3. Using wolfram_alpha calculate the Absolute Differences of Squares from the pair of integers from step 2
4. Using calculator find the difference between the results from step 3
5. Finish returning the result from step 4

'''


'''


1. Using wolfram_alpha determine the current date
2. Using wolfram_alpha calculate the number of days between the date from step 1 and the date from  last friday
3. Using time_series_intraday get the 'TSLA' weekly historical stock prices with the ending date obtained from step 2. The interval for the tool is 1 week.
4. Using tool wolfram_alpha filter the results from step to return two consecutive values in which the stock value is grather than 600
5. Using finish tool return a list with the pair of date in format YYYY-MM-DD HH:MM:SS and the corresponding value from setp 4.

'''



'''

663f382e5a3f548cd2a49d84

In the city with the oldest living tree, current date is 'September 26, 2023'. 
First you want to estimate the date of next full moon. 
Assuming the exact date of the full moon is not provided, we can approximate its date with this range: minus 2 days to plus 2 days of the calculated date. 
Using this estimated full moon date, provide the high and low temperature of that day in the city where the oldest living tree is found.
 Provide the number of days until this full moon.

 
1. Using wiki_search return only the city name and country of the oldest living tree

2. Using google_search search for the full moon date after on september 2023 in the city returned in step 1

3. If the date returned from step 2 is before 2023-09-26 using google_search search for the full moon date after on september 2023 in the city returned in step 1.

Else if the date returned from step 2 is after 2023-09-26 return the same result from step 2

4. Using historical_weather return the high and low temperature for the city name returned from step one in the date returned from previous step.

5. Using wolfram_alfa determine the number of days between the date returned on step 2 and 2023-09-26

6. Finish returning the results from step 3 and 4


Error - Please try again later. If that doesn't work, please contact support.


 
'''



'''
To find the most recent album by Adele, identify the release date of her latest album and then find out the second trading day after this date. 
What was the last trading date before the Sunday right after the second trading day? 
On that date, what was the closing price of Tesla shares at the close of the financial market?

1. Use wiki_search to retrive the most recent album by Adele, return the last trading date of the week after the relase date.
2. Use ticker_search to determine the symbol of Testla.
3. Use time_series_intraday to get the last result from closing price of the symbol obtained from step  in the date obtained from setp 1.
4. Finish returning the date and the price obtained from step 3.




1. Use google_search to retrive the most recent album date by Adele

2. Use ticker_search to determine the symbol of Testla.

3. Use time_series_intraday to get the last result from closing price of the symbol obtained from step 3 in the last trading day of the week after the date from step 1.

4. Finish returning the date and the price obtained from step 3.



'''

'''
This task required to iterate and filter the partial results with specific conditions. 
The pythoninterpreter tool would work for that but it is not avaiable in the platform.

'''


'''
663f382c4db6b0c74e08ee97

1. Using ticker_search determine the symbol of Testla and Airbus.
2. Using time_series_daily get the closing stock prices of Tesla and Airbus in the past 25 days.
3. Use calculator to calculate the dot product of the daily closing stock prices of each company obtained from the last step.
4. Use google_search to retrieve find the IPO date of European Aeronautic Defence and Space (EADS).
5. Finish returning the dot product obtained from step 3 and the IPO date obtained from step 4.

'''

{
"error": "",
"result": [
{
"timestamp": "2024-05-10",
"open_market_value": "163.0000",
"high_market_value": "163.3400",
"low_market_value": "159.8200",
"close_market_value": "159.8400",
"volume": "369966"
},
{
"timestamp": "2024-05-09",
"open_market_value": "161.2000",
"high_market_value": "162.3800",
"low_market_value": "160.5400",
"close_market_value": "162.3800",
"volume": "127247"
},
{
"timestamp": "2024-05-08",
"open_market_value": "159.8000",
"high_market_value": "162.8000",
"low_market_value": "159.5400",
"close_market_value": "161.6000",
"volume": "273029"
},
{
"timestamp": "2024-05-07",
"open_market_value": "158.1800",
"high_market_value": "158.9600",
"low_market_value": "157.1000",
"close_market_value": "158.8600",
"volume": "374864"
},
{
"timestamp": "2024-05-06",
"open_market_value": "154.3600",
"high_market_value": "156.8400",
"low_market_value": "154.3200",
"close_market_value": "156.6600",
"volume": "174434"
},
{
"timestamp": "2024-05-03",
"open_market_value": "154.5600",
"high_market_value": "155.5400",
"low_market_value": "153.4400",
"close_market_value": "154.2600",
"volume": "253016"
},
{
"timestamp": "2024-05-02",
"open_market_value": "154.0000",
"high_market_value": "154.6200",
"low_market_value": "153.1200",
"close_market_value": "153.5600",
"volume": "241708"
},
{
"timestamp": "2024-04-30",
"open_market_value": "156.2000",
"high_market_value": "156.9400",
"low_market_value": "154.6400",
"close_market_value": "154.6400",
"volume": "265470"
},
{
"timestamp": "2024-04-29",
"open_market_value": "157.7400",
"high_market_value": "157.8200",
"low_market_value": "154.1000",
"close_market_value": "155.9200",
"volume": "231550"
},
{
"timestamp": "2024-04-26",
"open_market_value": "157.9800",
"high_market_value": "158.2800",
"low_market_value": "153.7400",
"close_market_value": "157.0800",
"volume": "573440"
},
{
"timestamp": "2024-04-25",
"open_market_value": "162.2000",
"high_market_value": "162.3200",
"low_market_value": "157.0000",
"close_market_value": "158.4200",
"volume": "559513"
},
{
"timestamp": "2024-04-24",
"open_market_value": "162.1800",
"high_market_value": "164.6800",
"low_market_value": "162.1600",
"close_market_value": "162.1600",
"volume": "491396"
},
{
"timestamp": "2024-04-23",
"open_market_value": "162.7000",
"high_market_value": "162.9400",
"low_market_value": "160.6200",
"close_market_value": "162.6800",
"volume": "492033"
},
{
"timestamp": "2024-04-22",
"open_market_value": "160.3200",
"high_market_value": "161.5400",
"low_market_value": "159.5200",
"close_market_value": "161.4800",
"volume": "255514"
},
{
"timestamp": "2024-04-19",
"open_market_value": "158.1000",
"high_market_value": "160.8600",
"low_market_value": "157.6400",
"close_market_value": "159.9400",
"volume": "539735"
},
{
"timestamp": "2024-04-18",
"open_market_value": "161.1800",
"high_market_value": "161.6000",
"low_market_value": "158.9200",
"close_market_value": "160.6400",
"volume": "350028"
},
{
"timestamp": "2024-04-17",
"open_market_value": "158.9600",
"high_market_value": "161.5000",
"low_market_value": "158.5800",
"close_market_value": "159.8600",
"volume": "281688"
},
{
"timestamp": "2024-04-16",
"open_market_value": "158.9600",
"high_market_value": "159.5600",
"low_market_value": "157.3000",
"close_market_value": "158.9600",
"volume": "416389"
},
{
"timestamp": "2024-04-15",
"open_market_value": "163.9200",
"high_market_value": "165.3000",
"low_market_value": "162.8400",
"close_market_value": "163.6600",
"volume": "280224"
},
{
"timestamp": "2024-04-12",
"open_market_value": "163.5800",
"high_market_value": "165.2600",
"low_market_value": "162.4600",
"close_market_value": "162.9800",
"volume": "351501"
},
{
"timestamp": "2024-04-11",
"open_market_value": "164.3200",
"high_market_value": "165.5800",
"low_market_value": "161.5200",
"close_market_value": "162.1600",
"volume": "467920"
},
{
"timestamp": "2024-04-10",
"open_market_value": "164.5200",
"high_market_value": "165.1800",
"low_market_value": "162.7000",
"close_market_value": "164.2800",
"volume": "252251"
},
{
"timestamp": "2024-04-09",
"open_market_value": "170.0000",
"high_market_value": "170.3600",
"low_market_value": "164.3800",
"close_market_value": "164.6000",
"volume": "271822"
},
{
"timestamp": "2024-04-08",
"open_market_value": "168.5200",
"high_market_value": "171.1600",
"low_market_value": "168.5200",
"close_market_value": "170.5200",
"volume": "183733"
},
{
"timestamp": "2024-04-05",
"open_market_value": "167.0000",
"high_market_value": "168.0200",
"low_market_value": "165.2400",
"close_market_value": "168.0000",
"volume": "433654"
}
]
}


###############

'''
( 168.47 * 172.50) + ( 171.97 * 174.94) + ( 174.72 * 173.00) + ( 177.81 * 173.00) + ( 184.76 * 169.21) + ( 181.19 * 167.00) + ( 180.01 * 166.80) + ( 179.99 * 160.00) + ( 183.28 * 164.85) + ( 194.05 * 164.85) + ( 168.29 * 168.00) + ( 170.18 * 167.15) + ( 162.13 * 174.60) + ( 144.68 * 173.00) + ( 142.05 * 173.11) + ( 147.05 * 170.16) + ( 149.93 * 169.33) + ( 155.45 * 170.11) + ( 157.11 * 169.00) + ( 161.48 * 173.03)


{
"error": "",
"result": [
{

"temperature (°F)": "49.4669",
"temperature (°F)": "44.895645",
"temperature (°F)": "38.899403",
"temperature (°F)": "44.704403",
"temperature (°F)": "39.41315",
"temperature (°F)": "39.079403",
"temperature (°F)": "41.6894",
"temperature (°F)": "42.66065",
"temperature (°F)": "40.1744",
"temperature (°F)": "40.15565",
"temperature (°F)": "43.418148",
"temperature (°F)": "42.52565",
"temperature (°F)": "44.048153",
"temperature (°F)": "42.551903",
"temperature (°F)": "41.610645",
"temperature (°F)": "39.1544",
"temperature (°F)": "36.926903",
"temperature (°F)": "33.72815",
"temperature (°F)": "34.79315",
"temperature (°F)": "32.651897",
"temperature (°F)": "31.3169",
"temperature (°F)": "30.386904",
"temperature (°F)": "33.458153",
"temperature (°F)": "31.3694",
"temperature (°F)": "31.811903",
"temperature (°F)": "37.08815",
"temperature (°F)": "28.673147",
"temperature (°F)": "31.51565",
"temperature (°F)": "39.3119",
"temperature (°F)": "39.86315",
"temperature (°F)": "37.71065",



(49.4669 + 44.895645 + 38.899403 + 44.704403 + 39.41315 + 39.079403 + 41.6894 + 42.66065 + 40.1744 + 40.15565 + 43.418148 + 42.52565 + 44.048153 + 42.551903 + 41.610645 + 39.1544 + 36.926903 + 33.72815 + 34.79315 + 32.651897 + 31.3169 + 30.386904 + 33.458153 + 31.3694 + 31.811903 + 37.08815 + 28.673147 + 31.51565 + 39.3119 + 39.86315 + 37.71065)/31

'''