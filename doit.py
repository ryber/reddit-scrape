# -*- coding: utf-8 -*-
import praw
import os
from pprint import pprint

# installation:
# install all requirements with
#     'pip install -r requirements.txt'

if not os.path.exists('output'):
    os.makedirs('output')

def writeToFile(commentId, content):
    filename = "output/" + commentId + ".txt"
    file = open(filename,"w")
    file.write(content.encode('utf-8')) 
    file.close() 

# this is your oauth authenticated client. You need to set this up on redit and 
# fill in the client_secret and your user password
# see http://praw.readthedocs.io/en/latest/getting_started/authentication.html#script-application
reddit = praw.Reddit(client_id='dQJdVsQ5cf-kIg',
                     client_secret='',
                     password='',
                     user_agent='testscript by /u/fakebot3',
                     username='ryberrr')
                     

                     
submission = reddit.submission(url='https://www.reddit.com/r/programming/comments/8jjq33/11_best_programming_fonts/')                     
# pprint is a handy method to dump the data structure to screen so you can see what's in it.
# pprint(vars(submission))

# this code will output all the top-level comments, followed by second-level, third-level, etc. 
# http://praw.readthedocs.io/en/latest/tutorials/comments.html
submission.comments.replace_more(limit=None)
comment_queue = submission.comments[:]  # Seed with top-level
while comment_queue:
    comment = comment_queue.pop(0)
    writeToFile(comment.id, comment.body)
    comment_queue.extend(comment.replies)    
