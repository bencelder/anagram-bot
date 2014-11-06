import praw
from pprint import pprint

#r = praw.Reddit("anagram finder bot by Benjamin Elder v1.0")
#r.login('mr_chunderlust', 'crumpleshout')

r = praw.Reddit(user_agent="anagram finder bot by Benjamin Elder v1.0")
#submissions = r.get_subreddit("opensource").get_hot(limit=5)
comments = r.get_comments("all", limit = 1)

for x in comments:
    #pprint(vars(x))
    s_id = x
    c_id = x.id

#print c_id

cms = r.get_submission(url="https://www.reddit.com/r/pics/comments/2li4zq/_/clv3wfr")

cms = cms.comments

cmt = cms[0]

print cmt

#for x in cms:
    #pprint(vars(x))
