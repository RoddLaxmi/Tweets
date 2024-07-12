
import pandas as pd
from matplotlib import pyplot as plt
file = "C:\\Users\\roddl\\Code\\SampleData\\farmers_protest.json"
df = pd.read_json(file, lines=True)
users = pd.json_normalize(df['user'])
users.rename(columns={'id':'user_id','url':'profile_url'}, inplace=True)
users.drop(['description', 'linkTcourl'], axis=1, inplace=True)
users.head(5)
users = pd.DataFrame(users)
users.drop_duplicates(subset=['user_id'], inplace=True)
users.count()
user_id = [] 
for user in df['user']:
    uid = user['id']
    user_id.append(uid)
df['user_id'] = user_id
cols = ['url', 'date','renderedContent', 'id', 'user_id', 'replyCount','retweetCount', 'likeCount', 'quoteCount', 'source','media','retweetedTweet', 'quotedTweet','mentionedUsers']
tweets = df[cols]
tweets.rename(columns={'id':'tweet_id', 'url':'tweet_url'}, inplace=True)
tweets = pd.DataFrame(tweets)
tweets.drop_duplicates(subset=['tweet_id'],inplace=True)
tweets.shape[1]
df.to_csv("C:\\Users\\roddl\\Code\\SampleData\\structured_data.csv")
tweets_users = pd.DataFrame({1:[],2:[], 3:[], 4:[], 5:[]}) 
plt.scatter(tweets['date'], tweets['likeCount'])
plt.show()




