import praw
import re
import sys
import private
from util import read, write

def main():
    reddit = praw.Reddit(**private.config)

    print "Getting sub1 data.."
    sub1_data = get_comments(reddit, "republican", 125)

    print len(sub1_data)
    print "pickle sub1 data"
    write("sub1.raw", sub1_data)
    

    print "Getting sub2 data.."
    sub2_data = get_comments(reddit, "technology", 125)
 
    print len(sub2_data)
    print "pickle sub2 data"
    write("sub2.raw", sub2_data)


    if sys.argv[1] == "t":
        print "Getting sub3 data.."
        sub3_data = get_comments(reddit, "democrats", 125)
        print len(sub3_data)
        print "pickle sub3 data"
        write("sub3.raw", sub3_data)
    


def get_comments(reddit, subreddit, comment_count):
    sub_data = list()
    for submission in reddit.subreddit(subreddit).top(limit=comment_count):
        if submission.num_comments > 1:
            for comment in submission.comments.list()[:1]:
                if len(comment.body.split()) > 5 and len(sub_data) < 100:
                    sub_data.append((comment, subreddit))
    return sub_data



if __name__ == '__main__':
    main()