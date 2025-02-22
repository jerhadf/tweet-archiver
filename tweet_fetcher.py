#!/usr/bin/env python
# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
import csv

#Twitter API credentials
consumer_key = "2IJFyOCutbQeOdbyZSYhKybg1"
consumer_secret = "oM8B7G74vbZ9MeAdkSA55yyNrsfENQfpwQsEP25fk3Gk4BuFVi"
access_key = "2314821548-62KeWTntPGTdwByhYW7cK59q94ePIrY4DnJAytx"
access_secret = "WCJ8hp9qkjL5a9TqJvilU79r8rDhpBCd52PtX99gc7Ax6"

list_of_users_archived_already = ['AlyhaChan',
'DanielleFong',
'wildflowerearth',
'VPedro2020',
'rivatez',
'TylerAlterman',
'adamsafron', 
'SamoBurja',
'algekalipso',
'InquilineKea',
'lifeneoned']

list_of_users = [
    'ctbeiser', 
    'anderssandberg',
    'vkhosla', 
    'ID_AA_Carmack', 
    'alexandr_wang', 
    'hardmaru',
    'yashkaf', 
    'SimonDeDeo', 
    'LauraDeming', 
    'William_Blake', 
    'Plinz',
    'jessi_cata',
    'Meaningness',
    'tomaspetricek', 
    'Jonathan_Blow',
    'tomaspetricek'
]

def get_all_tweets(screen_name):
    #Twitter only allows access to a users most recent 3240 tweets with this method
    
    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    
    #initialize a list to hold all the tweepy Tweets
    alltweets = []    
    
    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=200)
    
    #save most recent tweets
    alltweets.extend(new_tweets)
    
    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1
    
    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print(f"getting tweets before {oldest}")
        
        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
        
        #save most recent tweets
        alltweets.extend(new_tweets)
        
        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        
        print(f"...{len(alltweets)} tweets downloaded so far")
    
    #transform the tweepy tweets into a 2D array that will populate the csv    
    outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]

    # print(outtweets)

    #write the csv
    with open(f'{screen_name}_tweets.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(["id","created_at","text"])
        writer.writerows(outtweets)
    
    pass
 
if __name__ == '__main__':
    #pass in the username of the account you want to download
	for user in list_of_users:
		get_all_tweets(user)