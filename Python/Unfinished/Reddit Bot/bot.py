import re, praw, webbrowser
from flask import Flask, request

r = praw.Reddit('StardustBot 0.1 by StardustGogeta')
r.set_oauth_app_info('24LGgSloifb81g','CIUXxicZmY-nr2svCqrpGK69i4w','http://localhost/')

app = Flask(__name__)


url = r.get_authorize_url('StarBot','save identity', True)
webbrowser.open(url)

@app.route('/')
def proc():
    webbrowser.open('http://127.0.0.1:5000/')
    link_no_refresh = r.get_authorize_url('StarBot','save identity')
    link_refresh = r.get_authorize_url('StarBot','save identity',True)
    link_no_refresh = "<a href=%s>link</a>" % link_no_refresh
    link_refresh = "<a href=%s>link</a>" % link_refresh
    text = "First link. Not refreshable %s</br></br>" % link_no_refresh
    text += "Second link. Refreshable %s</br></br>" % link_refresh
    return(text)

@app.route('/authorize_callback/')
def proc():
    return('Hello World!')
    code = request.args.get('code', '')
    access_information = r.get_access_information('FlrXqeggWN83FwUR5fLYI1NNm6M')
    print(access_information)
    r.set_access_credentials(**access_information)
    authenticated_user = r.get_me()
    print(authenticated_user.name, authenticated_user.link_karma)

app.run()

##with open("replies.txt", "r") as f:
##    replies = f.read()
##    replies = replies.split("\n")
##
##subreddit = r.get_subreddit('pythonforengineers')
##for submission in subreddit.get_hot(limit=2):
##    if submission.id not in replies:
##        if re.search("favorite movie\?$", submission.title, re.IGNORECASE):
##            submission.add_comment("""My favorite movie would have to be Star Wars.\n\n*****\n\nI am a bot. If you encounter any issues, please PM me at /u/StardustGogeta.""")
##            print("Bot replying to : " + submission.title)
##            replies.append(submission.id)
##with open("replies.txt", "w") as f:
##    for post_id in replies:
##        f.write(post_id + "\n")
