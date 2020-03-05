# In flask Shell

->>> from TWITOFF.models import *

->>> DB.create_all() # creates sqlite database! (only do once)

->>> u1=User(name='austen', id=5452)

->>> t1=Tweet(text='Go DSPT3 Cohort', id=3)

->>> DB.session.add(u1)

->>> DB.session.add(t1)

->>> DB.session.commit()

## Connecting to Twitter API in flask shell

->>> from TWITOFF.twitter import *

->>> twitter_user = TWITTER.get_user('elonmusk')

->>> tweets = twitter_user.timeline(count=200, exclude_replies=True, include_rts=False, mode='extended')
->>> tweets[0].text

## Basilica embedding tweet_text

->>> tweet_text = tweet[0].text

->>> embedding=BASILICA.embed_sentence(tweet_text,model='twitter')

->>> embedding

## Code to add tweets to db with embedding

->>> from TWITOFF.twitter import *

->>> twitter_user=TWITTER.get_user('elonmusk')

->>> tweets=twitter_user.timeline(count=200, exclude_replies=True, include_rts=False, tweet_mode='extended')

->>> db_user=User(id=twitter_user.id, name=twitter_user.screen_name, newest_tweet_id=tweets[0].id)

->>> for tweet in tweets:
...     embedding=BASILICA.embed_sentence(tweet.full_text,model='twitter')
...     db_tweet = Tweet(id=tweet.id, text=tweet.full_text[:500], embedding=embedding)
...     DB.session.add(db_tweet)
...     db_user.tweets.append(db_tweet)

->>> DB.session.add(db_user)
->>> DB.session.commit()

Aleks's notes

## in my terminal in main guthub repo for Day 4

pipenv shell

heroku login

heroku git:remote -a USERNAME-Twitoff

git remote --verbose

which gunicorn

gunicorn TWITOFF:APP

echo "web: gunicorn TWITOFF:APP -t 120" > Procfile

git add .

git commit -am "Deploying and adding Procfile

git push origin master

git push heroku master

heroku addons:create heroku-postgresql:hobby-dev

USERNAME-twitoof.herokuapp.com/reset #reset the database, create tables!
