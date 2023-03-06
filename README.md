# twitter_files
A. Steps:
1. Create a virtual environment
  pyenv virtualenv <YOUR_PYTHON_VERSION> twitter-env
  pyenv local twitter-env
  pip install --upgrade pip
  code .
2. Make the folder:
  mkdir -p ~/code/<username>/twitter-files && cd $_
3. Install the requirements
  pip install -r requirements.txt

Project scope:
1. Collect data from social media platforms
2. Store data in a database
3. Provide a REST API to access the data
4. Provide a web interface to access the data

Future capabilities:
1. Facebook: user profiles, groups, and communities (aka visitor posts)
2. Instagram: user profiles, hashtags, and locations
3. Mastodon: user profiles and toots (single or thread)
4. Reddit: users, subreddits, and searches (via Pushshift)
5. Telegram: channels
6. Twitter: users, user profiles, hashtags, searches (live tweets, top tweets, and users), tweets (single or surrounding thread), list posts, communities, and trends
