import praw
import random
import time

reddit = praw.Reddit(
    client_id="",
    client_secret="",
    user_agent="<console:bot:2.0>",
    username="",
    password=" "
)



subreddit=reddit.subreddit("television")

quotes=["Never,give up..!!!","Nothing in the world is perement","Live as if this is your last day"]
for submission in subreddit.hot(limit=5):
  
#for client_id,client_secret you'll have to create an account in reddit & got to 'https://www.reddit.com/prefs/apps' & you will find a tab in which 'are you a developer' apppears,click on that and enter details and create app,after that you will get a cliend_id,secret_id 



    for comment in submission.comments:
        if hasattr(comment,"body"):
         comment_lower=comment.body.lower()
        if "motivation" in comment_lower:
         print("--------")
        print(comment.body)
        random_index=random.randint(0,len(quotes)-1)
        comment.reply(quotes[random_index])
        time.sleep(6)


