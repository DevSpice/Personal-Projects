"""Hopefully my first working web scraper: not sure what I'm going to use this for"""

import requests
from bs4 import BeautifulSoup
import praw

url = 'https://www.reddit.com'
r = requests.get(url)
url_html = r.text

page = BeautifulSoup(url_html, 'html.parser')
for post in page.find_all('a'):
    # print(post)
    continue

    '''
    Important commands 
    
        all_comments = submission.comments.list()
        submission = reddit.submission("39zje0")
        submission.comment_sort = "new"
        top_level_comments = list(submission.comments)
        submission.add_comment('This is my comment')
        comment.reply('I'm replying to your comment')
    '''

## Using the reddit API
reddit = praw.Reddit(
    client_id='HG_c2-MuER2teZPVJLazBw',
    client_secret='uyARyCpfAb_rKPviIZR55PWLoVCbkQ',
    password='PythonTest1!',
    user_agent='Happy_Bot 1.0.0 - /u/Precious_Yellow_Snow',
    username='Precious_Yellow_Show',
)

class Subreddit:

    def __init__(self, subreddit, bot_text=[]):
        self.subreddit = reddit.subreddit(subreddit)
    
    def get_subreddit_info(self):
        """
        Gets the basic information of a subreddit and returns it in a print
        """
        print(self.subreddit.display_name)
        print(self.subreddit.title)
        print(self.subreddit.description)

    def get_top_submissions(self, depth=10, include_url=False):
        '''
        Gets the top submissions from the subreddit
        Depth is how many posts to get
        include_url contols whether the url to the post is included, defaults to false
        '''

        for submission in self.subreddit.hot(limit = depth):
            author = submission.author
            print('**********************************************')
            print(submission.title)
            print(author.name)
            print(submission.score)
            print(submission.id)
            if include_url:
                print(submission.url)
            print(' ')
            print('**********************************************')

    def get_top_submissions_list(self, depth=10, include_url=False):
        '''
        Gets the top submissions from the subreddit
        Depth is how many posts to get
        include_url contols whether the url to the post is included, defaults to false
        '''
        top_posts = {}
        for submission in self.subreddit.hot(limit = depth):
            self.author = submission.author
            title = submission.title
            score = submission.score
            id = submission.id
            top_posts[id] = (title, self.author, score)
        for i, _ in enumerate(top_posts):
            print(_)

    def get_comments(self, submission, depth=2):
        all_comments = submission.comments.list()
        for comment in all_comments():
            print(' ')
            print(comment.body)
            for second_level_c in comment.replies:
                print("    " + second_level_c.body)

            
solaire_text = [
    "I am Solaire of Astora, an adherent to the Lord of Sunlight."
    "Now that I am Undead, I have come to this great land, the birthplace of Lord Gwyn, to seek my very own sun!",
    " ",
]

darksouls3 = Subreddit('darksouls3', solaire_text)
# darksouls3.get_subreddit_info()
darksouls3.get_top_submissions(10)


