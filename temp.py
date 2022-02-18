import praw
import random
import time

reddit = praw.Reddit(
    client_id="iS3mSQTCu7Sd3imSmRPLrg",
    client_secret="vRsK2BLHUn1UXPZsylRkPs-KIQ5YeA",
    user_agent="<console:bot:2.0>",
    username="Personal-bot1234",
    password="paru123@"
)



subreddit=reddit.subreddit("television")

quotes=["Never,give up..!!!","Nothing in the world is perement","Live as if this is your last day"]
for submission in subreddit.hot(limit=10):
   # print("**************")
    #print(submission.title)

    for comment in submission.comments:
        if hasattr(comment,"body"):
         comment_lower=comment.body.lower()
        if "sad" in comment_lower:
         print("--------")
        print(comment.body)
        random_index=random.randint(0,len(quotes)-1)
        comment.reply(quotes[random_index])
        time.sleep(660)


