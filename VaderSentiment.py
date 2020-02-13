from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer 
import json
#_______Code complied by nikhil swami _______
#vader sentiment analysis code

#readymade block
def sentiment_scores(sentence): 
    # Create a SentimentIntensityAnalyzer object. 
    sid_obj = SentimentIntensityAnalyzer() 
    sentiment_dict = sid_obj.polarity_scores(sentence) 

    # print("Overall sentiment dictionary is : ", sentiment_dict) 
    print("SENTIMENT RATING ", sentiment_dict['neg']*100, "% Negative") 
    print("SENTIMENT RATING ", sentiment_dict['neu']*100, "% Neutral") 
    print("SENTIMENT RATING ", sentiment_dict['pos']*100, "% Positive") 
    print("OVERALL RATING", end = " ") 

    # decide sentiment as positive, negative and neutral 
    if sentiment_dict['compound'] >= 0.05 : 
        print("Positive") 
    elif sentiment_dict['compound'] <= - 0.05 : 
        print("Negative") 
    else : 
        print("Neutral") 
  
dicto1=json.load(open('processed.json','r'))
for item in dicto1['Posts']:
    #as described in the readme file some_dictonary['Posts'][i][j] // i=post number // j=3=post content
    sentence = item[3]
    print('\n',sentence)
    sentiment_scores(sentence)


