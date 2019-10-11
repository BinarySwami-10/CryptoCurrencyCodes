import json
import tweepy
import os
import tkinter
#_________________Contributed by Nikhil Swami____________________

# Authenticate to Twitter
auth = tweepy.OAuthHandler("0bEh2WjzKqYh4hIvQS6VwqIjR", 
    "BsOx7vXuDJ0m0zczSqfw4xftwvDOkbKrRTdReF9pTxpAbGW2Ms")
auth.set_access_token("1169646755190693888-2EbkmiYHfc4D6g9pubqlGH1u4PWoaE", 
    "2lCeBuYg8MNxCT85Bc5queSytSANJ6l62HJNpo5SB9J7D")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

#-----------------------AUTHENTICATION PHASE COMPLETED------------------------------
api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

tweet_dic={}
a=1
user = api.get_user("NatGeo")
name = "NatGeo"
tweetCount = 1111
results = api.user_timeline(id=name, count=tweetCount)
print('Profile Name:-')
print( user.name )


#----------------DATA EXTRACTION LOOP BEGINS-----------------------

for tweet in results:
    print(tweet.text)
    print('Date and Time of Tweet:-')
    print(tweet.created_at) #date of tweet
    print()
    tweet_dic[a]={"Tweet Text":tweet.text,"Tweet Date&Time":str(tweet.created_at)}
    a+=1

data={
      "User Name":name,
      "Profile Name":tweet.user.name,
      "Twitter ID":tweet.user.screen_name,
      "Bio":tweet.user.description,
      "Location":tweet.user.location,
      "URL":tweet.user.url,
      "Joined":tweet.user.created_at,
      "Following":str(tweet.user.friends_count),
      "Followers":str(tweet.user.followers_count),
      "Profile Image":tweet.user.profile_image_url_https,
      "Tweets":tweet_dic
      }


DataWrite = json.dumps(data, default=str)
json = open("Twitterdata.json",'w')
json.write(DataWrite)
json.close()

#------------USE LATER BLOCKS-----------------------------
'''
with open('Twitterdata1.json', 'w') as f:
  json.dump(tweet_dic, f, ensure_ascii=False)
'''

'''
print('Twitter ID:-')
print(tweet.user.screen_name+"\n")
print('Bio:-')
print(tweet.user.description+"\n")
print('Location:-')
print(tweet.user.location+"\n") 
print('URL:-')
print(tweet.user.url+"\n")
print('Joined:-')
print(tweet.user.created_at) 
print('Following:-')
print(str(tweet.user.friends_count)+"\n")
print('Followers:-')
print(str(tweet.user.followers_count)+"\n") 
print('Profile Image:-')
print(tweet.user.profile_image_url_https+"\n") 
print('Verification:-')
print(tweet.user.verified) #blue tick'''