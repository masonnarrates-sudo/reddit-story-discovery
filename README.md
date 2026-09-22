# reddit-story-discovery
Read-only Python tool for discovering and filtering public Reddit storytelling posts using the Reddit Data API.
# Reddit Story Discovery

Reddit Story Discovery is a small, locally run Python utility for discovering and filtering publicly available storytelling posts through the Reddit Data API.

## Purpose

The application helps manually review public submissions from selected storytelling and horror-related communities.

It is intended to support filtering by:

- Subreddit
- Post title
- Keywords
- Score
- Creation date
- Word count
- Estimated reading time

## Read-only design

This application is read-only.

It does not:

- Post submissions
- Comment
- Vote
- Send private messages
- Follow users
- Moderate communities
- Create accounts
- Access private subreddit content

Results are retrieved for manual review by the person running the application.

## Data used

The application may retrieve publicly available submission information including:

- Title
- Self-text
- Author username
- Subreddit
- Score
- Creation date
- Permalink
- Basic submission metadata

## Authentication

The application is designed to use approved Reddit API credentials and OAuth authentication.

API credentials are supplied through environment variables and are never stored in this repository.

## Usage

After Reddit API access has been approved:

1. Install the required Python packages.
2. Configure the Reddit API environment variables.
3. Run `story_finder.py`.
4. Choose a subreddit and review the returned public submissions.

## Compliance

This project is designed to respect Reddit API rate limits and Reddit's applicable developer policies.
