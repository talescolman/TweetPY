# pip install tweepy
import tweepy 
import time # always useful when using Twitter's API

# Authenticate to Twitter (always)
auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

# Create API object (always)
api = tweepy.API(auth)

# check if your authentications are working
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

# Create a tweet
api.update_status("Hello Tweepy")
api.update_status("Creating a Twitter bot")

# show the most recent 20 tweets in a timeline
timeline = api.home_timeline() # you can also put .items(250) if you want to print the 250 most recents tweets
for tweet in timeline:
    print(f"{tweet.user.name} said {tweet.text}")

# to see an user and its followers
user = api.get_user("user_name") #user_name = twitter account of the user you want to see

print("User details:")
print(user.name)
print(user.description)
print(user.location)

print("Last 20 Followers:")
for follower in user.followers(): #will show the name of the last 20 followers of that user
    print(follower.name)

# to follow an account
api.create_friendship("realpython") # will follow the realpython account

# update your biography
api.update_profile(description="I like Python")

# how to like the most recent twitter on your timeline
tweets = api.home_timeline(count=1)
tweet = tweets[0]
print(f"Liking tweet {tweet.id} of {tweet.author.name}")
api.create_favorite(tweet.id)

# see your blocked users
for block in api.blocks():
    print(block.name)

# see your muted users
for mute in api.mutes():
	print(mute.name)

# to block somebody
screen_name = # insert here the name of the user
api.create_block(user_id OR screen_name) # you should use either screen_name or user_id

# unblock an user
screen_name = # insert here the name of the user
api.destroy_block(screen_name or user_id) # you should use either screen_name or user_id

# to mute an user
screen_name = # insert here the name of the user
api.create_mute(screen_name or user_id) # you should use either screen_name or user_id

# to unmute an user
screen_name = # insert here the name of the user
api.destroy_mute(screen_name or user_id) # you should use either screen_name or user_id

# report as spam
screen_name = # insert here the name of the user
api.report_spam(screen_name)

# search 
for tweet in api.search(q="Python", lang="en", rpp=10): # rpp = the 10 most recent tweets with that word
    print(f"{tweet.user.name}:{tweet.text}")

# list the trend topics
trends_result = api.trends_place(1) # trends_place(1) means worldwide, to see the list of all the codes use api.trends_available()
for trend in trends_result[0]["trends"]:
    print(trend["name"])

# follow back everybody on your profile
for follower in tweepy.Cursor(api.followers).items():
    follower.follow()
    time.sleep(20) # remember to put your time sleep INSIDE your loops

# print all tweets using the cursor
for status in tweepy.Cursor(api.user_timeline).items(200):
    process_status(status)

# print all pages using the cursor
for page in tweepy.Cursor(api.user_timeline).pages(3):
    process_page(page)








