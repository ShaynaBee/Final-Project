# Final-Project

## Overview
### Background
Every day, over 500 million Tweets are Tweeted every day. Most of them will only be seen by a handful of people, but some of them are shared quickly by a large group of Twitter users. When this is the case, a Tweet is considered to be "going viral". The goal of this project is to develop a machine learning model that will be able to learn what makes a Tweet successful, and based on that, the model will eventually be able to produce high-quality Tweets that have a good chance to go viral.

#### Source of Data
The data used for this project will come from Twitter's API (developer.twitter.com).

#### Questions
- How capable is a machine learning model in analyzing what does or does not make a Tweet successful?
- Is it possible to go viral on Twitter with a machine-created Tweet?

#### Communication Protocols
Communication between team members will mainly be through Slack. Daily standups will be used to communicate individual daily contributions.

## Machine Learning Model

#### Scraping and Cleaning Data
The script to scrape tweets yielded about 1 million tweets, which were subsequently split in high success (>500 retweets) and low success categories.

#### RNN Model
The ML learning model was trained over 4 epochs.

![image](https://user-images.githubusercontent.com/93882635/166861179-4e31f882-8395-4fc8-89c7-84c79b12dea0.png)

#### Outcomes
The ML is currently able to produce tweets, but the quality seems problematic. The model relies heavily on learned patterns. When it recognizes a keyword, it will generate a historic tweet that starts with that keyword, rather than creating an original tweet. Also, it has happened that the prediction only contains emojis.

#### Challenges
- A web interface using flask was created to interact with the ML model, but at this time, it requires the ML to be run in its entirety, including training, which is very time consuming.
- It would be preferable to create Tweets using a keyword instead of starting word(s).
- The size of dataset used to train the model may seem big, but in reality only contains 2 days worth of tweets.
- The ML model is unable to take context into account. A lot of tweets are based on current events which our model does not know.
