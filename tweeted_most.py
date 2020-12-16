# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 09:23:17 2020

@author: Chaitali Patel
"""


from collections import Counter
#First Input: Take input for Number of test cases
test_cases = int(input()) 
user_name = []

final_result=[]   
for x in range(0,test_cases):
    #Second Input: Take input for Number of tweets
    tweets_cnt = int(input())
    user_name=[]
    for y in range(0,tweets_cnt) :
        #Third Input: Username and tweet id separated by space
        tweets = str(input())
        dum = list(tweets.split(" "))
        user_name.append(dum[0])
    
    counter = Counter(user_name)
   
     #Print user name and total number of tweets in given format
    times = Counter(counter) 
    repeat = times.values() 
    
    for element in set(repeat): 
    	dupl = ([(key, value) for
    			key, value in sorted(times.items()) if
    			value == element]) 
        
    	max_value = max(times.values()) 
        
    	temp_max_result = [(key, value) for
    					key, value in sorted(times.items()) if
    					value == max_value] 
        
    
    final_result.append(temp_max_result)

for x in final_result:
        #print(x)
        for (key,value) in x: 
            print (key,'',value) 

