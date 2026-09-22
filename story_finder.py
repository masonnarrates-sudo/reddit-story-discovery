import os
from datetime import datetime

import praw


SUBREDDITS = [
    "nosleep",
    "shortscarystories",
    "scarystories",
    "creepypasta",
]


def create_reddit_client():
    """Create an authenticated, read-only Reddit API client."""

    client_id = os.getenv("REDDIT_CLIENT_ID")
    client_secret = os.getenv("REDDIT_CLIENT_SECRET")

    if not client_id or not client_secret:
        raise RuntimeError(
            "Reddit API credentials are not configured. "
            "Set REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET "
            "after API access has been approved."
        )

    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent="windows:reddit-story-discovery:v1.0 (by u/MrMcGrinn)",
    )

    reddit.read_only = True

    return reddit


def word_count(text):
    return len(text.split())


def estimated_reading_minutes(text, words_per_minute=150):
    words = word_count(text)

    if words == 0:
        return 0

    return round(words / words_per_minute, 1)


def get_stories(reddit, subreddit_name, limit=25):
    """Retrieve recent public text submissions for manual review."""

    subreddit = reddit.subreddit(subreddit_name)

    stories = []

    for submission in subreddit.new(limit=limit):
        if not submission.is_self:
            continue

        body = submission.selftext or ""

        story = {
            "title": submission.title,
            "author": str(submission.author)
            if submission.author
            else "[deleted]",
            "subreddit": submission.subreddit.display_name,
            "score": submission.score,
            "created": datetime.fromtimestamp(
                submission.created_utc
            ).strftime("%Y-%m-%d"),
            "word_count": word_count(body),
            "reading_minutes": estimated_reading_minutes(body),
            "url": f"https://reddit.com{submission.permalink}",
        }

        stories.append(story)

    return stories


def display_stories(stories):
    for number, story in enumerate(stories, start=1):
        print("=" * 70)
        print(f"{number}. {story['title']}")
        print(f"Subreddit: r/{story['subreddit']}")
        print(f"Author: u/{story['author']}")
        print(f"Score: {story['score']}")
        print(f"Date: {story['created']}")
        print(f"Words: {story['word_count']}")
        print(f"Estimated narration time: {story['reading_minutes']} min")
        print(f"URL: {story['url']}")


def main():
    reddit = create_reddit_client()

    print("Reddit Story Discovery")
    print("----------------------")

    for subreddit in SUBREDDITS:
        print(f"\nSearching r/{subreddit}...\n")

        stories = get_stories(
            reddit,
            subreddit_name=subreddit,
            limit=10,
        )

        display_stories(stories)


if __name__ == "__main__":
    main()
