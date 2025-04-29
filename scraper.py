import praw
import reddit_secrets
import time

reddit = praw.Reddit(
    client_id=reddit_secrets.client_id,
    client_secret=reddit_secrets.client_secret,
    user_agent=reddit_secrets.user_agent,
    username=reddit_secrets.username,
    password=reddit_secrets.password
)

# Fetch the post
post_url = "https://www.reddit.com/r/askSingapore/comments/1k8dngd/why_do_you_support_opposition_serious_question/?share_id=NZdhY0853Zjrgjatxx23p&utm_content=1&utm_medium=ios_app&utm_name=ioscss&utm_source=share&utm_term=14"
post = reddit.submission(url=post_url)

# Check the total number of comments (including MoreComments objects)
post.comments.replace_more(limit=None)  # This ensures all comments are loaded
total_comments = len(post.comments)
print(f"Total comments available: {total_comments}")

# Scrape all comments
comments = []
for comment in post.comments:
    if isinstance(comment, praw.models.Comment):
        comments.append({
            'text': comment.body,
            'upvotes': comment.ups,
            'date': time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(comment.created_utc)),
            'author': str(comment.author) if comment.author else 'deleted'
        })

# Save the comments to a file for later processing
import json
with open('comments.json', 'w') as f:
    json.dump(comments, f, indent=4)

print(f"Scraped {len(comments)} comments.")